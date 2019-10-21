# CS_478_SemesterProject
Semester project for CS 478 Software Development

BDDT - Book and document Distribution Tool (BDDT) Proposal

## TOC

[Summary](#summary)<br>
[Feasibility](#feasibility)<br>
[Process](#process)<br>
[Audience](#audience)<br>
[UI](#ui)<br>
[Backend](#backend)<br>
[Roadblocks](#roadblocks)<br>

<div id='summary'/>

## Summary

The Book and Document Distribution Tool or referred to as BDDT for easier
recognition is our team proposal project that our group would like to research
and build. Our goal would be to provide a light user interface that can take any document a user submits and translate the text into an easy-reading format. This project will focus on users who have a poor internet connection, but would like to have information related ot a material of interest. This can be in the range from textbooks, manuals, and academic papers to fiction. 

<div id='feasibility'/>

## Feasibility

As we evaluated all other projects suggested, many of them we realized would probably take more than a semester to complete. The BDDT project we agreed upon represents a project we should be able to complete by the end of the semester as well as can be used by others outside the classroom. The user interface will be able to have a simplistic yet pleasing view for our audience and can have a different layout if the end user has a better internet connection. On the backend side, we only forsee a couple of problems involving how we will parse the text form the document, including if the document is uploaded or scanned. 

<div id='process'/>

## Process
The BDDT involves various steps from uploading to adhering a correct format. The
user will either submit a document that they wish to upload to our server or can go into our directory site to locate all the documents uploaded currently. If the user would like to submit a document for hosting they will click the button or drag their file into the space to begin the process.

As the document is uploaded to our webserver, our code will format the document, parsing out the images and collecting the raw text we want for displaying. The goal right now is to grab the text we want to display and remove the images (for the time being, we have also discussed of having a link added to access a separate page for the figure). We would expect our audience to use mobile devices than a computer for reading especially users out in the field who may need access to a manual. The document will then be on display using basic HTML and formatted correctly to where anyone who reads the corresponding document won't suffer unflattering paragraph format. A following diagram below explains our concept:

<img src="/BDDT.png">

*Figure 1: Lucidchart Diagram of the BDDT*

<div id='audience'/>

## Audience
This app is designed to help those who live in rural areas without fast 
internet connections. Compared to the rest of the world, other places have
to rely on speeds that can take hours to grab information let alone documents.
We believe this project would be useful for educators who teach in slow-connected areas or countries without a great infrastructure to allow high-speed internet. 

We also expect our audience to expand to others working in such countries who
may need to download manuals or references pertaining to their job at hand. From their perspective, they may not have the coverage to watch video tutorials relating to their 
subject at hand but can at least pull out a document.

<div id='ui'/>

## UI

We want our front end to look as dynamically pleasant as possible without 
causing a lack of time on already poor internet functions. For example, many modern sites add animations and other styles that although look fantastic for the site, would unfortunately be detrimental for our slow-end users. Therefore, we've proposed having two layouts. 

The basic homage would feature two or three buttons: submit a document, go to directory, and another that can give them the more dynamic website. The dynamic website option can also be included in the directory that when a user goes through their can search for documents. Our front end developers will concentrate on using HTML, CSS, and Angular for this part of the project. Some early examples of what the homepage and upload page may look like are seen below:

<img src="/homepage.jpeg">

*Figure 2: Proposed homepage for users*

<img src="/uploadpage.jpeg">

*Figure 3: Proposed upload page for users*

When a user goes into the directory page, they can see all the documents that have been uploaded to the website. Each one will have a title corresponding to their text uploaded and when they were uploaded. 

Discussion has also taken place about having a search bar in the directory as well as seeing the most recent documents being uploaded. Again, we are still stressing having a simple yet pleasing design that won;t be too hard on slow-end users. The other feature that goes beyond basic html will add more style and be available to faster end users.

<div id='backend'/>

## Backend
As a user submits their document, when they press the button we want our code to be able to decipher what type of file is being uploaded. We plan on using Python and its libraries to assist us in this portion of the project. When the document has been uploaded successfully, they should be able to find it in the directory page. How we order the directory page we are still in discussion about. We may also add a possibility of how the directory can be viewed for the end user (by author, recently updated, etc...).

<div id='roadblocks'/>

## Roadblocks
What we have discovered going over the project is what we will need to do
for parsing and formatting the material ranging from Word, PDF, and manual 
copy paste text. Will we have to tell the users that only certain extensions can be uploaded to our website? As in can we only take .pdf or .txt forms and nothing else?

How are we going to host the website? Since the files we are dealing with are
only text documents, we don't have to worry too much regarding space
capacity. This doesn't come into too much concern unless we are wanting to also keep the images that accompany the text as well. 

Do we know if we have a way of pulling out raw text from scanned files as well? Would this take some OCR software implementation that will be needed in our code as well?

