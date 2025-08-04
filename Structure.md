# Blog API Structure

## UI Structure

### Header

1. Logo
   1. UI/UX
      1. can accpet jpeg, jpg, png.
   2. Functions
      1. To represent company in a short and unique way
2. Company Name
   1. In bold letter and middle of the web page
3. Create Blog button
   1. UI/UX
      1. Vector Icons or Image Icons of Create means Plus button
      2. The border should rounded full
   2. Functions
      1. If user logged in it will go to another Page - Editor Page
      2. if user not logged in it will show user to login to create blogs
      3. shows small motivational qoutes to start blogging.
   3. Features
      1. isLoggedIn  ?  To route User to editor Page : To make user log in
4. Account Image
   1. UI/UX
      1. Images as  jpeg, jpg, png
   2. Functions
      1. if logged in show the routes and options user can visit
      2. if logged out take user to log in page or better be a modal
   3. Features
      1. Routes to account details page

### Body

1. Heading , Paragraphs , Italic, Bold, Underline (Html elements and attributes)
   1. UI/UX
      1. Heading will be bigger in size and Bold
   2. Function
      1. To captures viewers eye
      2. To define the blogs motive in few words
   3. Features
      1. Every heading will have a certain limit to upper size and have a certain limit for lowersize and h1 cannot be smaller than h2.
      2. Heading can be uppercase or lowercase but have to be in bold.
2. Editor will contain all these cases where cetain element cannot be smaller or greater than certain elements, Editors will have to use every elements of html, to make work and writing easy for writer.
3. Like and Comment
   1. UI/UX
      1. Text box will have textarea of html
      2. Button to submit
      3. Button to Like
      4. Like image will have multiple shapes like heart, support, thumbs up
   2. Features
      1. Like buttons should have shadow on hover
      2. Button should give a response on click like color change or color effect or ripple effect
      3. Text box should have placeholders for examples and should be expandable if comments goes more than 250 words then it should be visible to them.
      4. UI should be flexible according to device
   3. Functions
      1. Textbox should have state to maintain the text writter on it
      2. Text box should be able to correct gramatical mistakes
      3. Button of submit will submit the payload on Click
      4. Response should be given back to use that comment is done in a toaster way
      5. Comments will work like a feedback to writer.
      6. Comments can have links of other blogs and websites , can have youtube video links for reference
      7. Comments can be used as a publicity things or another way for writers to promote their article and themeselves.
4. Tags
5. Categories
6. Subjects

