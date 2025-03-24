# Potato Disease Prediction

## Project Overview  
This project focuses on detecting **potato leaf diseases** using a **Deep Learning** model. The trained **CNN model** classifies potato leaves into three categories:  
✅ **Healthy**  
🚨 **Early Blight**  
⚠️ **Late Blight**  

The model is deployed using **FastAPI** as the backend, with a frontend built using **HTML, CSS, and JavaScript**. Users can upload an image, and the system provides real-time predictions.  

---

## Dataset & Preprocessing  
- The dataset consists of images of potato leaves categorized into three classes.  
- Images are resized to **256x256** and normalized before training.  
- **Data augmentation** techniques such as **random flipping & rotation** were applied to improve generalization.  

---

## Model Architecture  
A **CNN model** was built using **TensorFlow & Keras**, featuring:  
- **6 Convolutional Layers** with **ReLU** activation  
- **MaxPooling** layers for downsampling  
- **Fully Connected Layers** with **Softmax activation**  
- **Adam Optimizer** with **Sparse Categorical Crossentropy**  

🚀 The final model was trained for **15 epochs** with an **80-10-10 Train-Val-Test split**.  

---

## How It Works?  
1️⃣ Upload an image of a potato leaf.  
2️⃣ The image is processed and passed to the **CNN model**.  
3️⃣ The model predicts whether the leaf is **Healthy, Early Blight, or Late Blight**.  
4️⃣ The result is displayed with a **confidence score**.  

---

## Tech Stack  
- **Python, TensorFlow & Keras** - Model Training  
- **FastAPI** - Backend  
- **PIL (Pillow)** - Image Processing  
- **NumPy & Matplotlib** - Data Handling & Visualization  
- **HTML, CSS, JavaScript** - Frontend (Integrated with FastAPI)  

---

🥔 This project is a **step towards helping farmers detect potato diseases early**, reducing crop losses & improving agricultural yield! 🌱  
