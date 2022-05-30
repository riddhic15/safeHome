# Safe Home App - Built during Microsoft Engage Mentorship Program 2022

*Project Demo Link* - ***https://drive.google.com/file/d/1Iz7IrT2musOWkGsx0pbTWj9Y7KIlKyME/view?usp=sharing***

![image](https://user-images.githubusercontent.com/58457452/170892553-ea3e4c5c-6778-4e5d-a927-2c92e9fe9ece.png)
    
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
   <li>
      <a href="steps-to-run-in-your-machine">Steps to run in your machine</a>
    </li>
    <li>
      <a href="#objective-behind-the-project">Objective behind the Project</a>
    </li>
    <li>
      <a href="#application-of-face-recognition">Application of Face Recognition</a>
    </li>
   <li><a href = "#features">Features</a></li>
   <li><a href="#features-description">Features Description</a></li>
      <ul>
        <li><a href="#add-member">Add Members</a></li>
        <li><a href="#confidenc-rating">Confidence Rating</a></li>
        <li><a href="#alert-system">Alert System</a></li>
        <li><a href="#away-mode">Away Mode</a></li>
       <li><a href="#home-mode">Home Mode</a></li>
      </ul>
   <li><a href="#home-page">Home Page</a></li>
      <ul>
        <li><a href="#landing-page">Landing Page</a></li>
        <li><a href="#about-section">About Section</a></li>
        <li><a href="#features-section">Features Section</a></li>
      </ul>
    <li><a href="#agile-methodology">Agile Methodology</a></li>
  </ol>
</details>

<!-- INSTALLATIONS -->

## Steps to run in your machine
To install and run the project on your local system, follow the given steps:

#### Run the following commands

1. Clone this repository
```
$ git clone https://github.com/riddhic15/safeHome.git
```
2. Change directory to safeHome
```
$ cd safeHome
```
3. Make sure you have python and flask installed in your system. Install all other dependencies that have been used in the project using pip:
```
pip install -r requirements.txt
```
4. Run the app
```
flask run
```
**NOTE: If you encounter an error saying module not found or an import error while importing app after running the 4th command, install the module that is not present using pip command.**

## Objective Behind the Project

The prime objective of this project is to combat the constant fear of any mishappening or crime taking place at our homes in our absence. My application, safeHome, through its monitoring system singlehandedly guarantees 24x7 complete security of the home even when no one is present. So, no longer do we need get daunted to leave home even if we have to stay away for days or months. 

## Application of Face Recognition

The main goal of the project is to prevent crime and help people lead a safer and stressfree life. Face recognition allows the application to recognise and remember the faces of added members. Thus, it is able to detect unrecognised people by distinguishing them from the added people who may have broken into the home with fraudulent intentions. So, this recognition technology combined with emotion recognition result in success of this project.

## Features
Some of the features included in this app are:

**Salient Features:**
- Two modes of Operation : Home Mode and Away Mode
- Live Alert system through mail on detecting unrecognised faces 
- Instantly add new faces
- Confidence Rating

## Features Description

### Add Member

Family members and friends can be added to the list of known people. After clicking add, about 100 pictures are captured which are then used to build dataset and train the model so as to recognise the people if they happen to be detected by the camera again. Names of people who have been recognised by the app, appear on the members page.

![image](https://user-images.githubusercontent.com/60353660/170885226-08038b0c-c9d5-49f4-ad4b-7da0decdb4aa.png)

![Screenshot (23)](https://user-images.githubusercontent.com/58457452/170893961-1e638eac-4426-4b47-9aa5-d66a5c24b6ec.png)
<!-- ![image](https://user-images.githubusercontent.com/60353660/170885529-aa270968-3453-4b00-bfa7-4ba975a27a5f.png)
 -->
![Screenshot (8)](https://user-images.githubusercontent.com/58457452/170893387-9aa2b5f8-cfed-49a3-96ed-2be67aa0d247.png)

### Confidence Rating

The confidence rating is a specialised feature developed to detect any unrecognised person whose intentions do not seem right on the basis of their facial expressions. This rating is calculated on the basis of whether the person is recognised or not and also on the basis of a person's facial expressions. So, any unrecognised person with fraudulent intentions will have a very low confidence rating less than 30% and owner will be alerted.

Shows a high confidence rating of 72% as the face is recognised.
![Screenshot (27)](https://user-images.githubusercontent.com/58457452/170894042-f01101f0-5804-423b-8e71-49ac2fae8f87.png)

### Alert System

As soon as the sytem detects an unrecognised face, it generates an alert and sends an email from safeHome account to the owner of the house along with the image of the stranger. Thus, the owner can take immediate action if any criminal or unknown person breaks into the house without their knowledge.

![mail](https://user-images.githubusercontent.com/58457452/170891311-8f7ccdcf-75ed-4d41-94fb-c87b10fb22dc.png)

<!-- ![image](https://user-images.githubusercontent.com/60353660/170885363-4bdaba47-546d-470d-9a3d-36842e6846a6.png) -->


### Away Mode

Monitors and ensures complete safety of home when the members are not at home. If it detects an unrecognised person, it displays a very low rating and mails the owner to warn them.

<p>Unrecognised:</p>
<img width = "800" align = "center" src = "https://user-images.githubusercontent.com/58457452/170892554-65991851-b4c8-45ca-b888-1fdb1bed87a2.png">

<p>Recognised:</p>
<img width = "800" align = "center" src = "https://user-images.githubusercontent.com/60353660/170885604-f7537d30-e195-46cc-a40b-a848a1a909df.png">

### Home Mode 

Monitors and ensures complete safety of home when the members are at home. 

![image](https://user-images.githubusercontent.com/60353660/170885078-aec71f80-3119-4927-a1d7-1321c0c2a7c3.png)


## Home Page

### Landing Page

![image](https://user-images.githubusercontent.com/58457452/170892556-995001d5-53e3-45b0-a265-85556b7345d5.png)

### About Section

![image](https://user-images.githubusercontent.com/58457452/170892557-f63a4ab0-94d6-4275-b814-1a6b0ad9cda9.png)

### Features Section

![image](https://user-images.githubusercontent.com/58457452/170892558-6738ebe6-39eb-4b0f-aac1-297d9e582d7d.png)

## Agile Methodology

In accordance with the principles of Agile Methodology, this project has been built in four sprints spread evenly over the four weeks of the mentorship program. I had a roadmap ready for each week beforehand so as to systematically build the project in a planned manner.

![image](https://user-images.githubusercontent.com/60353660/170884774-4acbcc57-051a-489a-ad1e-cfc9a890cd95.png)

<br></br>
