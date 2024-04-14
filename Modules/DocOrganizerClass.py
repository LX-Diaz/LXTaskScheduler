import shutil, os
from datetime import datetime



class DocumentOrganizer:
    def __init__(self):

        self.Drives = {"Volume1": 'D',
                  "Volume2": 'E',
                  "Volume3": 'F'}
        self.FORMATS = {
            "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                       ".heif", ".psd"],
            "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".MP4", ".webm", ".vob", ".mng",
                       ".qt", ".mpg", ".mpeg", ".3gp", ".MOV"],
            "DOCUMENTS": [".oxps", ".pages", ".docx", ".doc", ".fdf", ".ods",
                          ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                          ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                          "pptx", ".txt", ".in", ".out", ".csv", ".html5", ".html", ".htm", ".xhtml"],
            "ARCHIVES": [".a", ".ar", ".cpio", ".tar", ".gz", ".rz", ".7z",
                         ".dmg", ".rar", ".xar", ".zip"],
            "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                      ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
            "LIBRARY": [".pdf", ".epub", ".mobi"],
            "XML": [".xml"],
            "APPLICATIONS": [".exe", ".msi"],
            "SCRIPTS": [".sh", ".ahk", ".py", ".bat"],
            "DISK_IMAGE": [".iso", ".img"],
            "3D_FILES": [".stl", ".obj", ".gcode", ".fdx", ".x3d", ".wrl", ".blend"]
        }

        # Select Drive to clean. Drives "Volume 2" and "Volume 3" should not be touched by this program yet
        #self.DRIVE = input(f"Select Drive to organize: {self.Drives.keys()}")

        #self.SELECT_DRIVE = f"{self.Drives[self.DRIVE]}:/"
        self.SELECT_DRIVE = f"{self.Drives['Volume1']}:/"

        self.DIRECTORIES = {"ARCHIVES": f"{self.SELECT_DRIVE}Documents/Compressed_Archives",
                       "DISK_IMAGE": f"{self.SELECT_DRIVE}Disk_Images",
                       "APPLICATIONS": f"{self.SELECT_DRIVE}Applications",
                       "Downloads": f"{self.SELECT_DRIVE}Downloads",
                       "DOCUMENTS": f"{self.SELECT_DRIVE}Documents",
                       "LIBRARY": f"{self.SELECT_DRIVE}Documents/Electronic_Library",
                       "AUDIO": f"{self.SELECT_DRIVE}Music",
                       "IMAGES": f"{self.SELECT_DRIVE}Pictures",
                       "VIDEOS": f"{self.SELECT_DRIVE}Videos",
                       "3D_FILES": f"{self.SELECT_DRIVE}3D Objects",
                       "Dir_1": f"{os.getcwd()}",
                       "SCRIPTS": f"{self.SELECT_DRIVE}_scripts"
                       }
        self.log = open(f"{self.DIRECTORIES['Dir_1']}/log.txt", "a")

    def ChkDir(self):
        print('Checking for desired directories...')
        self.log.write(f"\n{'-' * 30}\n{str(datetime.now())}\nChecking for desired directories...\n{'-'* 30}")
        for folderName in os.walk(self.SELECT_DRIVE):
            if os.path.exists(self.DIRECTORIES["ARCHIVES"]) and \
                    os.path.exists(self.DIRECTORIES["DISK_IMAGE"]) and \
                    os.path.exists(self.DIRECTORIES["APPLICATIONS"]) and \
                    os.path.exists(self.DIRECTORIES["Downloads"]) and \
                    os.path.exists(self.DIRECTORIES["DOCUMENTS"]) and \
                    os.path.exists(self.DIRECTORIES["LIBRARY"]) and \
                    os.path.exists(self.DIRECTORIES["AUDIO"]) and \
                    os.path.exists(self.DIRECTORIES["IMAGES"]) and \
                    os.path.exists(self.DIRECTORIES["VIDEOS"]) and \
                    os.path.exists(self.DIRECTORIES["3D_FILES"]) and \
                    os.path.exists(self.DIRECTORIES['SCRIPTS']) and \
                    os.path.exists(f"{self.DIRECTORIES['Dir_1']}/log.txt"):
                print('Directories found, proceed...')
                self.log.write(f"\nDirectories found, proceed...")
                self.log.close()
                break
            else:
                print('Directories were not found...')
                print(f"\nMaking dir:{self.DIRECTORIES['ARCHIVES']}")
                self.log.write(f"\nMaking dir:{self.DIRECTORIES['ARCHIVES']}")
                try:
                    os.mkdir(self.DIRECTORIES["ARCHIVES"])
                    print('Created:' + 'Compressed_Archives')
                except FileExistsError:
                    print("Directory Compressed_Archives exists. Continuing")

                print('Making dir:' + self.DIRECTORIES["SCRIPTS"])
                try:
                    os.mkdir(self.DIRECTORIES["SCRIPTS"])
                    print('Created:' + '_scripts')
                except FileExistsError:
                    print("Directory _scripts exists. Continuing")

                print('Making dir:' + self.DIRECTORIES["DISK_IMAGE"])
                try:
                    os.mkdir(self.DIRECTORIES["DISK_IMAGE"])
                    print('Created:' + 'DISK_IMAGE')
                except FileExistsError:
                    print("Directory Disk_Images exists. Continuing")

                print('Making dir:' + self.DIRECTORIES["APPLICATIONS"])
                try:
                    os.mkdir(self.DIRECTORIES["APPLICATIONS"])
                    print('Created:' + 'APPLICATIONS')
                except FileExistsError:
                    print("Directory Applications exists. Continuing")

                print('Making dir:' + self.DIRECTORIES["LIBRARY"])
                try:
                    os.mkdir(self.DIRECTORIES["LIBRARY"])
                    print('Created:' + 'Electronic_Library')
                except FileExistsError:
                    print("Directory Electronic_Library exists. Continuing")
                try:
                    self.log = open(f"{self.DIRECTORIES['Dir_1']}/log.txt", "w")
                    self.log.write('All required directories accounted for... Proceed to organize')
                    self.log.close()
                    print()
                except:
                    pass
                print('All required directories accounted for... Proceed to organize')


    def CCleaner(self):
        # Run CCLEANER
        self.log = open(f"{self.DIRECTORIES['Dir_1']}/log.txt", "a")
        self.log.write(f"\n{'-' * 30}\n{str(datetime.now())}\n{'-'* 30}")
        os.chdir("C:\Program Files\CCleaner")
        os.system('cmd /c "CCleaner64.exe/AUTO"')
        print('\n' + "Ran CCleaner...")
        self.log.write('\n' + "Ran CCleaner...")
        self.log.close()

    def Organize(self):
        # Move working directory to Downloads folder
        os.chdir(self.DIRECTORIES['Downloads'])
        print('Current directory: ' + os.getcwd())
        self.log = open(f"{self.DIRECTORIES['Dir_1']}/log.txt", "a")
        self.log.write('\n' + "-" * 30 + '\n' + str(datetime.now()) + '\n' + "Organized Files" + '\n' + "-" * 30)
        for key in self.FORMATS:
            for filename in os.listdir(self.DIRECTORIES['Downloads']):
                for items in self.FORMATS[key]:
                    if filename.endswith(items):
                        try:
                            shutil.move(filename, self.DIRECTORIES[key])
                            self.log.write('\n' + f"{filename} moved to {self.DIRECTORIES[key]}")
                            print('\n' + f"{filename} moved to {self.DIRECTORIES[key]}")
                        except:
                            os.remove(filename)
                            self.log.write('\n' + f"{filename} could not be moved to {self.DIRECTORIES[key]}...DELETED")
                            print('\n' + f"{filename} could not be moved to {self.DIRECTORIES[key]}")
                            pass
        print(f"\nProcess Complete...\nReview log file : {self.DIRECTORIES['Dir_1']}/log.txt for more details")
        self.log.write(f"\nProcess Complete...\nReview log file : {self.DIRECTORIES['Dir_1']}/log.txt for more details")
        self.log.close()

