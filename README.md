# Face Blur

## ระบบการตรวจจับใบหน้าเพื่อเบลอใบหน้าที่ไม่ต้องการให้ปรากฎ

---

## การติดตั้ง

** จำเป็นต้องติดตั้ง Conda ก่อน สามารถดูวิธีการติดตั้งได้ที่ https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages  
  
ถ้าหากติดตั้ง Conda แล้วให้รันคำสั่งด้านล่างเพื่อทำการสร้าง Environment และติดตั้ง Package  
  
สร้าง environment

```sh
conda create -n attendance python=3.8
conda activate attendance
```

ติดตั้ง package

```sh
pip install scikit-learn opencv-python mtcnn tqdm pandas numpy keras_facenet imutils matplotlib seaborn glob tensorflow joblib 
```

## โครงสร้าง

* ``buffer/`` เป็นโฟลเดอร์สำหรับเก็บ buffer ที่ใช้ในการ debug ดูแต่ละ frame ของการ detect / recognize จากโมเดล
* ``dumped_model/`` เป็นโฟลเดอร์สำหรับเก็บ feature vector, labels และ optimizer ที่ dump ไว้ใช้ในการ run โมเดล
* ``images/`` เป็นโฟลเดอร์สำหรับเก็บรูปภาพที่ใช้ในการ train โมเดล
* ``models/`` เป็นโฟลเดอร์สำหรับเก็บโมเดล ไว้ referenced และ weights สำหรับการใช้งานโมเดลนั้นๆ
* ``scripts/`` เป็นโฟลเดอร์สำหรับเก็บ script ที่ใช้ในการ automate task ต่างๆ
* ``videos/`` เป็นโฟลเดอร์สำหรับเก็บวิดีโอที่ใช้ในการ test / debug model

## การเตรียมข้อมูล

ทำการ run script สำหรับ generate รูปภาพของ user โดย script จะอยู่ที่ ``scripts/data-generation/``

```sh
cd scripts/data-generation
datagen-train-test-val.py
```

จากนั้นทำกรอกชื่อของ user, โฟลเดอร์ที่ต้องการ generate รูปภาพ (train, test, val) และจำนวนรูปภาพที่ต้องการ generate

download weight ของ pre-trained model VGGFace : https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5 และใส่ไฟล์ดังกล่าวที่โฟลเดอร์ ``model/``

( สำหรับรูปการเทรนของผู้จัด : https://drive.google.com/file/d/1WkoMd609x31sNnF49CNn4OIDtnvyjrzn/view?usp=drive_link )

นำรูป 1 รูปของ user ที่ต้องการ recognize ใส่ไว้ที่ folder ``images/euclidean/``

นำ video ที่ต้องการเบลอใส่ไว้ใน folder ``videos``

## วิธีการใช้งาน

ทำการ run cell ที่ 1 - 4 ของ file python notebook main-deepface.ipynb โดย cell ที่ 5 ใช้สำหรับการ detect ใบหน้าเท่านั้น และ cell ที่ 6 - 7 ใช้สำหรับการ recognize ใบหน้าโดยสำหรับ cell ที่ 6 จะมีการเก็บ log ใบหน้าในแต่ล่ะเฟรมไว้
