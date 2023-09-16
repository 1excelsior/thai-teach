# Thai Teach
#### Video Demo:  <https://www.youtube.com/watch?v=GqBxJhy8Pj0>
#### Description:

My partner is a Thai teacher on a particular online teaching platform. She once playfully said that it would be nice if somehow, I can apply the knowledge from CS50x to make her teaching process more efficient. Although she wasn't serious about the request, it has become an inspiration for my final project since then.


#### Folder Contents
Aside from README.md, there are 4 files and 3 children folders containing their respective files in the project folder.


**flask session**
A folder for storing sessions

**static**
Contain a custom CSS stylesheet

**templates**
Contains 7 html files as follows
1.add.html = a page whose sole purpose is to let admins add a new word to the database. It contains three text bars and an Add button.
2.apology.html = function precisely as the one in Finance. It produces a grumpy-looking cat meme with an error code and corresponding text.
3.edit.html = a page that allows admins to edit details regarding each word such as its pronunciation, its meaning in English, or the Thai spelling itself.
4.export.html = a page that allows any user to export words of their choice, adjustable with a delete button corresponding to each word showing in the list and a clear button to clear all words.
5.index.html = the main page of the website. It contains a search bar for searching a word and a select button corresponding to each word displayed in the result table
6.layout.html = a layout that reduces repetitive coding.
7.login.html = a login page for admins (essential for accessing hidden features).

**app.py**
The file that utilizes Flask to host a dynamic website and define every routing.

**helpers.py**
Defines apology and login required as in Finance

**requirments.txt**
Preloading necessary modules

**thaidict.db**
There are only two tables in the whole database, the users and the words. Essentially, Thai Teach is basically a personalized Thai dictionary with assists my girlfriend's work and her student's learning process in mind. As such, the words table was created by converting my girlfriend's teaching materials into CSV. before importing them into the SQL database, resulting in a database with about 1600 Thai words in it.

Additionally, the users table contains two admin accounts, one for my partner, and another for myself; each account has exclusive access to hidden features that guests or general users won't have (more about this part later).


#### Features
All features of this web application can be categorized into two big groups; general features for every user (including guests and admins) and exclusive features for admin/teacher.

##### General Features
Without logging in, every user will have access to three web pages including the homepage, the export page, and the log-in page named "For Teacher" on the navbar.

1.Word Search: as a general feature, the homepage consists of a search bar that can search corresponding words for a keyword; a keyword can be either Thai or English; to be precise, the Thai input will likely correspond to an existing Thai word in the "Thai" column of the words table while English would likely correspond to a data in whether "Pronunciation" or "Meaning"; leaning on the latter. Any corresponding word will be displayed in a table with 3 columns identical to the words table in thaidict.db

2.Exportation: By clicking a select button corresponds with a resulted word and its hidden id value, the word will be routed to the export.html via post method, making it possible for users to copy the words by highlighting and copy-paste them in a designated destination such as in a word doc, excel file, plain text file, chat box, etc. Nevertheless, the page comes with a corresponding delete button for each selected word and a clear-all button for convenient use.

##### Exclusive Features
By logging in through a form of the login page, there are 2 hidden features that will become available.

1.Word Adding: As the name suggests, you will be able to add new words via add.html's form. By providing 3 text bars with a value and then clicking the Add button, the details will be logged into the words table accordingly.

2.Word Editing/Deletion: A new edit button will appear behind each resulting word. By clicking it, you will be routed to an edit.html, this page allows you to edit any detail regarding the word such as its meaning in English, its pronunciation, and even its Thai spelling with a simple click on the Save Change button. Additionally, if you deem the word unneeded, you may delete it via the Delete button.

# thai-teach
