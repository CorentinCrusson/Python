import os, time, shutil

def detectChange(path_to_watch,path_to_destinate):    
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        time.sleep (5)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        
        if added: 
            print("Added: ", ", ".join (added))
            for a in added:
                moveFile(path_to_watch+'\\'+a,path_to_destinate+'\\'+a)
                print("Moved : {}".format(a))
        if removed: 
            print("Removed: ", ", ".join (removed))

        before = after
def moveFile(source,destination):
    shutil.move(source, destination)

if __name__=="__main__":
    detectChange(r"C:\Users\Corentin\Downloads",r"D:\Projet\GEL PECHE\0 - Divers\Schematisation")