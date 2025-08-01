Old Photo Colorization API
A FastAPI-based web service to automatically colorize old black-and-white photos, making them vivid and lifelike using deep learning models.

📸 Before and After

<table>
<tr>
  <td><b>Original</b></td>
  <td><b>Colorized</b></td>
</tr>
<tr>
  <td><img src="https://github.com/diyanaikk/image-colorization-api/blob/main/examples/pic1.jpg?raw=true" width="300"/></td>
  <td><img src="https://github.com/diyanaikk/image-colorization-api/blob/main/examples/colorized_pic1.jpg?raw=true" width="300"/></td>
</tr>
</table>


⚙️ Features
+ Upload a grayscale photo through FastAPI's default /docs UI.
+ Automatically saves both the original and colorized images.
+ Uses licensed pretrained ML models for colorization.
+ Easy to use with a minimal API interface.

🛠 Tech Used
+ Python
+ FastAPI
+ Pretrained colorization model
+ OpenCV for image handling

🧪 How to Use
+ Step 1: Clone the repo and install dependencies :
pip install -r requirements.txt
+ Step 2: Run the FastAPI server : 
uvicorn app.main:app --reload
+ Step 3: Open FastAPI Docs UI : 
Visit: http://127.0.0.1:8000/docs
+ Step 4: Upload an Image:  
  - Scroll to the /colorize-image/ POST endpoint.  
  - Click "Try it out"  
  - Upload your grayscale image (.jpg, .png, etc.)  
  - Click "Execute"  
  - You’ll receive the file path to the colorized image, saved under the static/uploads/ folder.


🔖 License Disclaimer
The colorization model files used in this project are the intellectual property of Richard Zhang et al. and are shared for academic and research purposes.
We have not modified or trained these models ourselves.
Original model source: https://github.com/richzhang/colorization

👩‍💻 Author
Diya Naik
[@diyanaikk](https://github.com/diyanaikk)
