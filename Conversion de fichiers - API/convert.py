import cloudconvert
import sys

def init():
    pass
    
def main(fic,frmt):
    api = cloudconvert.Api('j1FXpcE7GZrISh9BjzaSF6Y3lylcvsJb9opigTFEr0DdKScCADf4l2QvJlQckk0P')
    process = api.convert({
        'inputformat': fic[fic.index('.')+1:],
        'outputformat': frmt,
        'input': 'upload',
        'file': open(fic, 'rb')
    })

    process.wait()
    process.download(fic[:fic.index('.')]+'_Convert'+'.'+frmt)
    
    return      
    

if __name__=="__main__":
    if len(sys.argv)>1:
        if len(sys.argv)>2:
            main(sys.argv[1],sys.argv[2])
        else:
            print("\n_______________\nJe rappelles que c'est ==> convert.py documentAConvertir formatDeConversion <==")
    else:
        print("\n_______________\nVeuillez indiquez des choses car là ..")
