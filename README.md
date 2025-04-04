[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4Y4_rQdn)
# CP1404 Assignment 2 - Song List 2.0 by YOUR_NAME

A Python project with GUI and Console programs that (re)use classes to manage a list of songs to learn.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you?

The entire project took approximately 15–20 hours to complete. This included time spent on designing the program structure, implementing the required functionality, debugging, and writing the reflection. The bulk of the time was spent on integrating Kivy for the GUI, ensuring proper class design, and handling edge cases in the song management logic.

## 2. What are you most satisfied with?

I am most satisfied with the modularity and reusability of the code due to the use of Object-Oriented Programming (OOP). By creating separate Song and SongCollection classes, I was able to cleanly separate data representation (Song) from data management (SongCollection). This separation made it easier to implement both the console-based and GUI-based versions of the program without duplicating logic.

Additionally, I am pleased with how the GUI aligns well with the OOP principles. Using Kivy's dynamic widget creation and event handling allowed me to create an interactive interface where adding or toggling songs feels seamless.

## 3. What are you least satisfied with?

While the project met all the requirements, I struggled with some aspects of the GUI implementation. Specifically:

Aligning the heights of widgets between the left and right columns proved challenging at first. It required careful adjustment of size_hint, height, and minimum_height properties.
Handling dynamic updates in the ScrollView when adding or toggling songs was initially tricky. I had to ensure that the song_list was cleared and rebuilt correctly to avoid UI inconsistencies.
Although these issues were resolved, they consumed more time than expected. In hindsight, I could have experimented with smaller test cases earlier to streamline this process.

## 4. What worked well in your development process?

Several aspects of my development process worked well:

* Incremental Development: Breaking down the task into smaller components (e.g., creating the Song class first, then the SongCollection, and finally integrating them into the GUI) helped manage complexity.
* Testing Early and Often: Writing unit tests for the Song and SongCollection classes ensured their correctness before moving on to the GUI.
* Using Version Control: Git was instrumental in tracking changes and experimenting with different approaches without fear of losing progress.
* Documentation as I Went: Adding comments and docstrings throughout the code made it easier to revisit and understand specific parts later.

## 5. What about your process could be improved the next time you do a project like this?

There are several areas where I believe my process could improve:

* Planning: While I sketched out the general structure of the program, I underestimated the challenges posed by the GUI integration. Spending more time upfront planning the layout and interactions would have saved time during implementation.
* Prototyping: For future projects involving GUIs, I plan to prototype small sections of the interface early to identify potential issues sooner.
* Refactoring Earlier: Some parts of the code became slightly convoluted as new features were added. Refactoring earlier would have maintained cleaner code throughout development.

## 6. Describe what learning resources you used and how you used them.

To complete this assignment, I relied on various learning resources:

* Kivy Documentation: The official Kivy documentation was indispensable for understanding how to use layouts, widgets, and event handling. I frequently referenced examples and explanations for concepts like ScrollView, BoxLayout, and property binding.
* Online Tutorials: Watching tutorials on YouTube and reading articles on Medium helped clarify certain aspects of Kivy, such as dynamically creating buttons and managing scrollable content.
* Course Materials: The CP1404 lecture slides and practical exercises provided foundational knowledge about OOP and GUI programming in Python.
* Stack Overflow: When encountering specific issues (e.g., height mismatches or event handling), Stack Overflow often had relevant answers or suggestions.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

### Challenge 1: Height Mismatch Between Columns

* Obstacle: Initially, the widgets in the right column (song list) appeared shorter than those in the left column (controls). This was due to inconsistent height settings and improper handling of minimum_height in the ScrollView.

* Solution: After reviewing Kivy documentation and testing different configurations, I explicitly set the height of each song button to sp(40) and ensured the song_list BoxLayout dynamically adjusted its height using self.minimum_height. Additionally, spacers (Widget with size_hint_y: 1) were added to both columns to ensure equal stretching.


### Challenge 2: Dynamic Widget Updates

* Obstacle: Updating the song list after adding or toggling a song initially caused visual glitches (e.g., overlapping buttons).

* Solution: To resolve this, I cleared the existing widgets in the song_list BoxLayout and recreated them from scratch whenever the song collection changed. This ensured consistency and eliminated redundant widgets.


### Challenge 3: Edge Case Handling

* Obstacle: Input validation for the "Add Song" feature was prone to errors if users entered invalid years or left fields empty.

* Solution: I implemented robust input validation checks in the add_song() method. These checks displayed appropriate error messages and prevented invalid entries from being processed.

## 8. Briefly describe your experience using classes and if/how they improved your code.

Using classes significantly improved the structure and maintainability of my code. Here’s why:

* Encapsulation: The Song class encapsulates all attributes and behaviors related to individual songs, while the SongCollection class manages the entire collection. This separation of concerns makes the code easier to read and modify.
* Reusability: Both the console-based and GUI-based programs rely on the same Song and SongCollection classes. This eliminates redundancy and ensures consistency across implementations.
* Extensibility: With a solid class foundation, adding new features (e.g., filtering or exporting songs) would be straightforward in future iterations of the program.
