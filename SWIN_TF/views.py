from django.http import HttpResponse
from django.shortcuts import render
from TF.models import image_table
from django.core.files.storage import FileSystemStorage


import torch
from torchvision import transforms as T 
from PIL import Image
import timm

img_process = T.Compose([ # We dont need augmentation for test transforms
            T.Resize(256),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(timm.data.IMAGENET_DEFAULT_MEAN, timm.data.IMAGENET_DEFAULT_STD), # imagenet means
            ])


def predict(model, path, img_process, classes):
    print(path)
    image = Image.open(path)
    image = img_process(image)
    image = torch.unsqueeze(image, axis=0)
    output = model(image)
    output = torch.argmax(output)
    output = classes[output.item()]
    return output

def home(request):
    return render(request, "home.html")

def models(request):
    return render(request, "models.html")

def leaf(request):
    return render(request, "leaf.html")

def forest(request):
    return render(request, "forest.html")

def butterfly(request):
    return render(request, "butterfly.html")

def flower(request):
    return render(request, "flower.html")


def predictImage(request):
    
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    # print(filePathName)
    
    model = torch.jit.load('./models/butterfly_swin_transformer.pt')
    classes = []    
    path = "."+filePathName
    label = predict(model, path, img_process, classes)
    data = {'filePathName':filePathName, 'predictedLabel':label}
    return render(request, "models.html", data)

def predictleaf(request):
    folder = "leafDiseaseData/"
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(folder+fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    # print(filePathName)
    model = torch.jit.load('./models/canvas_leaf_disease.pt')
    classes = ['Cassava Bacterial Blight (CBB)', 'Cassava Brown Streak Disease (CBSD)', 'Cassava Green Mottle (CGM)', 'Cassava Mosaic Disease (CMD)', 'Healthy']
    path = "."+filePathName
    label = predict(model, path, img_process, classes)
    data = {'filePathName':filePathName, 'predictedLabel':label}
    return render(request, "leaf.html", data)


def predictforest(request):
    folder = "FireImageData/"
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(folder+fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    # print(filePathName)
    model = torch.jit.load('./models/Fire_detect_Transformer.pt')
    classes = ['fire', 'nofire']    
    path = "."+filePathName
    label = predict(model, path, img_process, classes)
    data = {'filePathName':filePathName, 'predictedLabel':label}
    return render(request, "forest.html", data)


def predictbutterfly(request):
    folder = "ButterflyData/"
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(folder+fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    # print(filePathName)
    model = torch.jit.load('./models/butterfly_swin_transformer.pt')
    classes = ['ADONIS', 'AFRICAN GIANT SWALLOWTAIL', 'AMERICAN SNOOT', 'AN 88', 'APPOLLO', 'ATALA', 'BANDED ORANGE HELICONIAN', 'BANDED PEACOCK', 'BECKERS WHITE', 'BLACK HAIRSTREAK', 'BLUE MORPHO', 'BLUE SPOTTED CROW', 'BROWN SIPROETA', 'CABBAGE WHITE', 'CAIRNS BIRDWING', 'CHECQUERED SKIPPER', 'CHESTNUT', 'CLEOPATRA', 'CLODIUS PARNASSIAN', 'CLOUDED SULPHUR', 'COMMON BANDED AWL', 'COMMON WOOD-NYMPH', 'COPPER TAIL', 'CRECENT', 'CRIMSON PATCH', 'DANAID EGGFLY', 'EASTERN COMA', 'EASTERN DAPPLE WHITE', 'EASTERN PINE ELFIN', 'ELBOWED PIERROT', 'GOLD BANDED', 'GREAT EGGFLY', 'GREAT JAY', 'GREEN CELLED CATTLEHEART', 'GREY HAIRSTREAK', 'INDRA SWALLOW', 'IPHICLUS SISTER', 'JULIA', 'LARGE MARBLE', 'MALACHITE', 'MANGROVE SKIPPER', 'MESTRA', 'METALMARK', 'MILBERTS TORTOISESHELL', 'MONARCH', 'MOURNING CLOAK', 'ORANGE OAKLEAF', 'ORANGE TIP', 'ORCHARD SWALLOW', 'PAINTED LADY', 'PAPER KITE', 'PEACOCK', 'PINE WHITE', 'PIPEVINE SWALLOW', 'POPINJAY', 'PURPLE HAIRSTREAK', 'PURPLISH COPPER', 'QUESTION MARK', 'RED ADMIRAL', 'RED CRACKER', 'RED POSTMAN', 'RED SPOTTED PURPLE', 'SCARCE SWALLOW', 'SILVER SPOT SKIPPER', 'SLEEPY ORANGE', 'SOOTYWING', 'SOUTHERN DOGFACE', 'STRAITED QUEEN', 'TROPICAL LEAFWING', 'TWO BARRED FLASHER', 'ULYSES', 'VICEROY', 'WOOD SATYR', 'YELLOW SWALLOW TAIL', 'ZEBRA LONG WING']
    path = "."+filePathName
    label = predict(model, path, img_process, classes)
    data = {'filePathName':filePathName, 'predictedLabel':label}
    return render(request, "butterfly.html", data)

def predictflower(request):
    folder = "FlowerData/"
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(folder+fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    # print(filePathName)
    model = torch.jit.load('./models/Flower_SWIN_Transformer.pt')
    classes = ['alpine sea holly', 'anthurium', 'artichoke', 'azalea', 'balloon flower', 'barberton daisy', 'bee balm', 'bird of paradise', 'bishop of llandaff', 'black-eyed susan', 'blackberry lily', 'blanket flower', 'bolero deep blue', 'bougainvillea', 'bromelia', 'buttercup', 'californian poppy', 'camellia', 'canna lily', 'canterbury bells', 'cape flower', 'carnation', 'cautleya spicata', 'clematis', "colt's foot", 'columbine', 'common dandelion', 'common tulip', 'corn poppy', 'cosmos', 'cyclamen ', 'daffodil', 'daisy', 'desert-rose', 'fire lily', 'foxglove', 'frangipani', 'fritillary', 'garden phlox', 'gaura', 'gazania', 'geranium', 'giant white arum lily', 'globe thistle', 'globe-flower', 'grape hyacinth', 'great masterwort', 'hard-leaved pocket orchid', 'hibiscus', 'hippeastrum ', 'iris', 'japanese anemone', 'king protea', 'lenten rose', 'lilac hibiscus', 'lotus', 'love in the mist', 'magnolia', 'mallow', 'marigold', 'mexican petunia', 'monkshood', 'moon orchid', 'morning glory', 'orange dahlia', 'osteospermum', 'passion flower', 'peruvian lily', 'petunia', 'pincushion flower', 'pink primrose', 'pink quill', 'pink-yellow dahlia', 'poinsettia', 'primula', 'prince of wales feathers', 'purple coneflower', 'red ginger', 'rose', 'ruby-lipped cattleya', 'siam tulip', 'silverbush', 'snapdragon', 'spear thistle', 'spring crocus', 'stemless gentian', 'sunflower', 'sweet pea', 'sweet william', 'sword lily', 'thorn apple', 'tiger lily', 'toad lily', 'tree mallow', 'tree poppy', 'trumpet creeper', 'wallflower', 'water lily', 'watercress', 'wild geranium', 'wild pansy', 'wild rose', 'windflower', 'yellow iris']
    path = "."+filePathName
    label = predict(model, path, img_process, classes)
    data = {'filePathName':filePathName, 'predictedLabel':label}
    return render(request, "flower.html", data)