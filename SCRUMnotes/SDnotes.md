## Overview

Front end
---------
Angular
HTML/CSS
Sass?

### Backend

- Python
- Tesseract

### Implementation questions

- Will need some sort of database
- Solution: Keep a raspberry pi storing all the documents
- Could also be hosting through githun using jekyll
- How long do we want to keep this up for? either for the software project or for a while?
- Possibly using AWS depending on the using Lambda which would figure the coputation
- Also can use S3 buckets to host the website 

### What we want this to do
- Joseph's lucidchart
- What will the goals be for each person
- Everyone by the end should understand both frontend and backendo works


## 9/06/19

### Notes regarding
- having a beasic layout like wordpress
- pleasing to the eyes but no images
- have links to most recent pdfs
- Plus having sections for more either text manuals or education literature
- about us page
- have two different layouts: basic and more styling
- can choose depending on Internet connection
- could detect what internet connection speed is and make recommendation
- may add depeding on connection speed (may be fancier)
- how we want our powerpoint
- Summary/How it Works/Front End/Back end/Roadblocks/ FAQ or questions
- Each team will be using seperate development environment

### 9/16

- User story and code design can be paralell san starting together
- Tesseract will probably be used for most of the backend
- Issue? Architecture, we still need to flesh out wha tthe front ends so the backend works correctly
- Solution: May need strings or depending on common variable
- May use a gloabl variable for catching or need a container for testing 
- Agree on a common set of interface or global variable
- Hand off or fetch location when pressing the button instead of just put inside the code
- Some intemediary for fetching the code
- Splits the problem into teams instead of everybody having to join in to figure out the problem
- That way if anything needs to be changed on front end or back end, can be done by either team
- Problem which could have: could save original and output storage
- Can run into storage prblem
- Document should be able to handle the lambda function
- Another way: We take the API call
- Hand the function to the file where we take care of everything else
- AWS using lambda functions which is great for code that runs occasionaly but not often
- Make API - Hand the doucment to the function and with the type - won't need anything
- Easier on user and the front end

### Conclusion:
- May have to research how AWs could grab a file without going through our server
- May need to find a file for handling services
- We will choose one
- Do research how file handling works for research (either team)
- If tesseract will be used, need to handle output and clean it up again
 Time Estimate: 15 minutes


### 9/18

- Clear emphasis on user story
- Entry in and acts like a trail for us
- Checking out different file formats
- SFTP or other?
- Do we consider a different protocol on file transfer?
- May fall under the code design and the userstory is for what would the user see
- Possibly a drag and drop
- We have two main paths upload and download paths
- View webpage path and upload page path
- chocie if they wanted the extra privacy
- may let them choose url name?
- Big hole in our knowledge base: How are we gonna handle the upload?
- Have them deliver the document to us
- brings us to permissions
- May need to look at a terms of service
- Have our own moderation
On front end
------------
- how will the front end look
- rough representation of the directory 

9/20/19
- Will need a domain name
- AWS for file transfer protocol and how its uploaded
- we have a documentation
- Pcik a good name 
- Next Friday, come up with your final name
- Hopefully something better than BDDT
- We will be breaking everything down into user story for next time.
- Develop the user story with the Lucid chart
- May have to split work for backend and frontend 
- Stretch goal - Add some text for a summary of the link
- Descriptive files names encouraged
- Preferred documents uploaded
- On homepage tell user what would be preferred for uploading document
- Can also use XML for formatting
- Can show them a preview of what it will look like 
- Can let user choose how the format to be

Goal for next time
--------------------
- Rough draft of the user story
- Check something into git
- How we will handle text other than pdf

9/23/19
-------
- Authentication will be difficult to set up
- amintainence should be fine
- Signing andautentication documentation for AWS
- Probably setup a student account for our website
- may able to set up to expire
- just need a general security
- wire frame is starting getting 
- By Wendesday start throwing something for the user story
- User story template for both backend/frontend started
- Have preliminery for the backend schematic and frontend schematic 


9/27/19
-------
- Jira too much of a pain, may go with Trello
- DFD and user story online, need everone to take a look and either add or delete what needs to be included
- Trello provides better tracking aspects
- Proibably need an admin, either Hans or Joseph
- Ideas are getting planned out
Tasks
-----
- Joseph setting up trello
- Hans finish final draft on userstory and DFD
- Jace/Kaitlynn starts building index files (Kaitlyn on directory/ Jace on index page)
- Al parsing method and the scheduler

9/30/19
-------
- CSS style how much will be a question
- Text display what CSS are we gonna display
- Make it easier to read
- Backend will grab the text
- frontend will choose how to display the text
- Hans will set up the trello impact
- Discussed what we want for front page to view, upload, and check recent documents
- Make the website backwards compatible, this is due to our users may be on expired or out-of-date windows

10/02/19
---------
- Got additions for Trello
- Beginning tasks have been added
- Kaitlyn has a mock up of the directory
- Jace has his upload on the github branch
- Al has the parse method down and formatting just has to be covered
- Now working on the stylesheet

10/10/19
- Demo I due in two weeks
- we will have the home page
- Add a documentation link (doesn't have to be huge)
- Still need to figure out the triggering function of the lambda
- Will get the bucket up and running
- Filtering out still a question
- Copyright still a problem, (rules will still be manual moderators)

10/14/19
- Have a demo of the site up through amazons s3 bucket
- Account may have to be renewed
- Progress made on the website can be copied over
- Uploading the file will do nothing
- Index.html page on Jace's page for github
- Angular has the site set up differently 
- Al progress can parse the pdf
- Everything that is handled on the page is in python script
- May conflict with s3 bucket if not javascript
- may have to have our own pi server for it as well
- Still need to see how it works on the project side
- Next thing would be to expand the parsing for other file formats

10/16/19
- Confident that front end can present there pages for demo on next Friday
- Al's parser is working correctly remoteley
- Need to finish up the upload part
- move Al's parser into the AWS Lambda
- do we have a particular page to merge the page
- demo will have a fuctioning upload page 
- file backend for upload 
- We have the beginning and end but still need the middle for the directory
- parser stores the html, generates an html file, and what is sent back is an html file
- Formatting will be off, but at least be consistent
- May have the back with a border

10/18/19
- Jace's index file needs to work with Al 
- try to get al's branch to work on lambda
- Jospeh will be working the lambda to put Al's parser in
- Upload page will be uploaded tonight for Al's code

10/30/19
- SQL question needs to be rsearched
- Homepage will probably go through some transition
- How do want the user to interface 
- Would SQL be the best case to use with S3 bucket?
- What could make s3 and SQL compatibile
- Athena may be something, but may be a paid 
- Do we waht to keep an SQL database for the file directory?
- Information only needs a link?
- Specwise what do we want to do?
- What capability do we want to give them for the directory 
- How do we want them to search
- What kind of search do we want to give them
- Do we want to give them a textbox search or a key/password?
- Hard part of the search, do we want to restrict the search
- Should we give them a search at all? which would give them?
- We may have to implement the user?
- How do you filter out the public and private?
- Six digit code is technically a user?
- Everythings open, but have a strong enough url?
- Possibly Cloudfare that can bloack ip addresses
- Do we want the private section at all?
- SureFire 
- They keep track of the users, not us.


## 11/01/19

- Roadblock concerning integrating the database
- Concerns that if a user wants to browse the public directory while finding private documents
- This would require building a database for the login, usernames, passwords, and more
- Great concept, but not enough time
- If a user wants a private document, we give them a url string
- url hyperlink is unique and acts as a username/pw
- link takes them to the webpage, moving away from the database.
- Let the user choose, private by default
- User fills categories for title, author, and genre minimum
- SQL database question regarding AWS Lambda
- Review AWS documentation (Hans) and Kaitlyn tests
- Front end, may add hamburger menu for mobile users

## 11/04/19

- discovery of solution regarding SQL database
- requires using AWS Relational Database Tables (RDS)
- Can hold capabilities of asp.net
- Hans researching some tutorials on how to integrate database

## 11/06/19

- Kaitlyn has cleaned up database of the private filters
- Revamped part of the front end
- Miscommunication on one end
- Hans believed all the documents would display on directory page
- Hans and Kaitlyn had to draw our diagram to see end result.
- Hamburger format keeps going off page
- Questions regarding directory wildcards from Al
- can we catch the specifics of what we need or will the user have to type in the exact matches

## 11/08/19

- Two weeks before the demo
- Hans will be trying to rebuild database for asp.net
- Believes he can get a connection, but may rebuild it from his computer
- Joseph running into problems with flask and the S3 bucket
- Could be referenced to using permissions
- Can get the parser working, but only on localhost
- Have new milestones
- 11/15 find someway to connect the database from S3
- 11/18 Merge upload page and Al's code

## 11/11/19

- Hans rebuilt and added other features to the database
- Could connect to the database on AWS RDS
- could not get the database to appear after linking the combinations
- May believe it has something to do with permission errors
- Al beginning research on how to search within the document. 

## 11/13/19

- On frontend side, Jace will revamp the file upload and homepage
- Adding new functionality
- Kaitlyn's database originally couldn't link up
- After Hans's testing and rebuild, still couldn't get it to hook up.
- May end up just testing on local host.
- Al's continuing his research on searching using Solr

## 11/15/19

- Jace has finished his changes on the upload page
- Will begin merging his code with Al's backend
- Joseph still running into problems uploading the document to S3
- May be to the naming conventions with Flask
- Been making progress, but a more problems kept creeping. 

## 11/18/19 

- Al has gotten the merge with Jace's upload page
- May keep the display as is for the Choose File/ Upload File
- Can only work right now but the template will hide it if the button goes to the bottom
- Page gets parsed and is routed to a directory where the parsed document stays
- Random string is generated for text document
- Joseph can get the document to be put into an s3 bucket
- May put the s3 bucket public
- Anyone can then check it out
- Will at that point just put a wrapper around it
- Technically a site but wrapped. 


## 11/20/19 
- Al has integrated Solr searching
- We can search both the document and keywords inside the document
- Joseph can get the files to go into the S3 bucket
- Can actually find the parsed document
- Can display how much the files get condensed.

