from PIL import Image,ImageDraw
import face_recognition as f
import pickle
import os 
from os import path

known_encodings = []
known_names = []

for i in range(1,122):
    try:
        if os.path.exists("./known/" + str(i)+".jpg"):
            img = f.load_image_file("./known/" + str(i)+".jpg")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)

        elif os.path.exists("./known/" + str(i)+".png"):
            img = f.load_image_file("./known/" + str(i)+".png")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)

        elif os.path.exists("./known/" + str(i)+".jpeg"):
            img = f.load_image_file("./known/" + str(i)+".jpeg")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)


        elif os.path.exists("./known/" + str(i)+".JPG"):
            img = f.load_image_file("./known/" + str(i)+".JPG")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)

        elif os.path.exists("./known/" + str(i)+".PNG"):
            img = f.load_image_file("./known/" + str(i)+".PNG")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)

        elif os.path.exists("./known/" + str(i)+".JPEG"):
            img = f.load_image_file("./known/" + str(i)+".JPEG")
            img_encode = f.face_encodings(img)[0]
            known_encodings.append(img_encode)
            known_names.append(str(i))
            print(i)



        else: 
            print("Photo " + str(i)+" not found")
    except Exception : 
            print("Error occured while opening file")


fn = 'encode.dat'    
fna = 'name.dat'


with open(fn,'wb') as data:
    pickle.dump(known_encodings,data)


print(known_names)

with open(fna,'wb') as names:
    pickle.dump(known_names,names)

