import numpy
import cv2 
import os

def center_crop(img, crop_width,crop_height):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	crop_width,crop_height: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img

def modify_frame(frame,size):
    """Returns modified image
	Args:
	frame: image to be modified
	size: dimensions (width, height) to be cropped
	"""
    modified_frame= center_crop(frame,size[0], size[1]) 
    modified_frame = modified_frame[::-1,::-1] #Espelha a imagem
    modified_frame= numpy.transpose(modified_frame,(1,0,2)) #Rotaciona 90º
    return modified_frame

def get_frames_save(video_dir, video_name, output_dir):
    video_path = os.path.join(video_dir, video_name)
    #os.path.splitext(filename):This function splits the filename into a tuple: (root, extension).
    #os.path.splitext(filename)[0] gives the root (the filename without the extension).
    output_name=f"{os.path.splitext(video_name)[0]}_out.mp4"

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
       
    w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #another way: height= frame.shape 
    h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    size = (int(w/2),int(h/2)) 
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')

    if not os.path.exists(output_dir):
      os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, output_name)
    out=cv2.VideoWriter(output_path,fourcc,new_fps,(size[1],size[0]))

    curr_frame = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        # if frame is read correctly check_captura is True
        if not ret: 
            print("Can't receive frame (stream end?). Exiting ...")
            break

        if curr_frame % int(round(fps / new_fps)) == 0: #fps=25,fps_new=1: mostra de 25 em 25 frames
            frame=modify_frame (frame, size)
            
            cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
            #frame = cv2.resize(frame, (960, 540))                # Resize image
            cv2.imshow('Frame', frame)
   
            out.write(frame) # Write the frame into the file 'output.mp4' 
            if cv2.waitKey(1000) == ord('q'): #espera 1 segundo pela tecla q se não vier continua
                break
        curr_frame += 1
    cap.release()
    out.release()
    cv2.destroyAllWindows()

     
new_fps = 1# Target Keyframes Per Second
video_dir ="C:\\Users\\Dan\\Documents\\Bewatcher\\Atividades\\Atividade1\\videos\\original"
video_name="shop_lifter_n_10.mp4"
output_dir="C:\\Users\\Dan\\Documents\\Bewatcher\\Atividades\\Atividade1\\videos\\output"

get_frames_save(video_dir, video_name, output_dir)
