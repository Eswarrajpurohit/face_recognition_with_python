from PIL import Image,ImageDraw
import face_recognition as f
import pickle
import datetime
#import database

def Rec_std(path):

    # Loading data from binary files  
    with open('encode.dat','rb') as data : 
          Std_Encodings =  pickle.load(data)
    with open('name.dat','rb') as n : 
          Std_names =  pickle.load(n)     
    
    print(datetime.datetime.now())  
    
    try :
        # Fetching image that has to be recognized 
        image = f.load_image_file(path)
        
        # if image is present then fetch locations and encoding 
        face_locate = f.face_locations(image)
        face_encoding = f.face_encodings(image,face_locate)

        pillow_image = Image.fromarray(image)

        draw = ImageDraw.Draw(pillow_image) 
        
        i = 1
        for (top,right,bottom,left),faces, in zip(face_locate,face_encoding):
            name = "Unknown Person"
            
            match = f.compare_faces(Std_Encodings,faces,tolerance=0.4)
            
            if True in match: 
                index = match.index(True)
                name = Std_names[index]
                #database.insertRecord(lec_id,name,1,fac_id)
                

            draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

            #to draw for lable
            height=draw.textsize(name)
            draw.rectangle(((left,bottom - height - 10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
            draw.text((left  +6,bottom - height-5),name,)
            i += 1

        print(datetime.datetime.now())
        print(Std_names)
        del draw

        pillow_image.show()
        pillow_image.save('test.jpg')

    except Exception as e:
        print("Error : \n")
        print(e)
 
 #if __name__ == "__main__":
print("Enter ther path of the Image : ") 
path = input()
Rec_std(path)     