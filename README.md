# Fake-Detect Servers
Contains <b>Flask</b> and <b>ASP.NET backend implementations</b> for Fake Social Detection AIML mini project.
Currently, only the Flask implementation is added. The reason for implementing with Flask is that ASP.NET isn't learned by any of the developers involved, and having a simple Flask implementation will help make the development quick when the developers eventually start building the ASP.NET backend. 
<stonrg>However only the <code>/predict</code> route is implemented in the current versions.</strong>

# Routes to build in the backend:
<ol>
<li>
/predict: <i>(implemented)</i><br /> 
<ol>
<li>
Page that takes inputs from user, predicts genuineness using the pre-trained model, and returns the prediction back to the user.
</li>
<li>
<strong>(Feature Addition): Update this page to accept not only the 8 account details individually, but also a test.csv dataset to predict a bunch of test-records at the same time</strong>
</li>
</ol>
</li>
<li>/dataset:<br /> Page that displays the training dataset.</li>
<li>/graph:<br /> Page that displays the training-accuracy & loss graph to the user.</li>
</ol>
