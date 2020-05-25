### PROJECT NAME
galla
### PROJECT AUTHOR
Suad Mohamed 
### DESCRIPTION
galla a personal gallery where you can upload  detailed images,with location and different categories,
it allows users to view thr posted photos, and select them based on the location where the photo were taken or the category of the photos..
## PREREQUISITES (CLONING & RUNNING)
ou need to do the following to start working on the project on your local computer:
A computer running on either Windows, MacOS or Ubuntu operating you can do the following:

1. Clone the application using git clone(this copies the app onto your device).In terminal:

          $ git clone
          $ cd suad'sgallery

2. Creating the virtual environment:  

          $ python3.6 -m venv virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py |python
3. Installing Django and other Modules:

         $ python3.6 -m pip install -r requirements.txt

4. Run the application:

          $ python3 manage.py runserver

### TESTING THE APPLICATION
1. To run the tests for the class files:

          $ python3.6 manage.py test 

### PROJECT SETUP INSTRUCTION   
- Clone this repository to your local computer.
- Ensure you have python3.6 installed in your computer.       
- From the terminal navigate to the cloned project folder.
### TECHNOLOGIES USED
* Django
* Python3.6
* Bootstrap3
* SQLAlchemy
### DEPLOYING (LIVE LINK)

### BEHAVIOR DRIVEN DEVELOPMENT (SPECIFICATIONS)
| Behaviour |  Input | Output |
| :---------------- | :---------------: | :------------------ |
| Display Photos | On page load | List of various photos  |
| Display Photos Details | On click photo | List of photos details 
| Display photos with title| search for:food,yoga & clothing |  list of images with description & posted time display.
| Display photos Details | On click image |image category,description & location display
| Navigate back to home page | On click navbar-brand suad's gallery| Display list of photos.   |                       |   

### CONTACT
sm.ha21@hotmail.com
### LICENSE 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

he above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
