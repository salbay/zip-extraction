from zipfile import ZipFile

def extraction(path,destination):
    parsed = path.split("/")
    fixed_parsed = parsed[-1][0:-4]
    with ZipFile(path,"r") as object:
        object.extractall(destination)