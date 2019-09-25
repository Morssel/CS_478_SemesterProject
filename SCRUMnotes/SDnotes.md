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
- how will the front end look?
- rough representation of the directory?