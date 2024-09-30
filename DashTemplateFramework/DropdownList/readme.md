# Dropdown List
Dropdown list allows users to select predefined selctions, both single and mutliple selections.

## Modules
### dashboard_singleSelection.py
This module allows user to select a choice from a dropdown list, along with a call function.

<img src=single_dropdown.png>

### dashboard_multipleSelections.py
This module allows user to select one or more choices from a dropdown list, along with a call function.

<img src=multipleSelections_dropdowns.png>

### dashboard_multidropdowns.py
This module places two dropdown lists side-by-side, and display both selections in the text box below the dropdown list.

<img src=multiple_dropdowns.png>

<br><br>
Note: Adding <b>display:inline-block</b> in the Divs' style parameter to set two Divs to place side-by-side. 

### dashboard_diff_label_value.py
This module allows user to select a choice from a dropdown list, along with a call function. The function will capture the value assoication with the selection, instead of the selection label itself.

<img src=dropdown_diff_label_value.png>

### dashboard_placeholder_dropdownlist.py
This module allows developers to place the instruction as placeholder in the dropdown list and disable users to clear the selection.

<img src=dropdown_placeholder.png>

### dashboard_disablesearch_dropdown.py
This moduel prevents users to type and search for their selection, but to select only from the dropdown list.

<img src=dropdwon_disablesearch.png>

## How the example works?
### Example 1 - Single Selection
Select a choice from the dropdown list, and it will display it in the text box below the dropdown list.

### Example 2 - Multiple Selections
Select the choice(s) from the dropdown list, and it will display all the selection in one string in the text box below the dropdown list.

### Example 3 - Multiple Dropdown List in one Row
Select a choice from either dropdown list, and the choices will be display in the text box below dropdown list. The dropdown lists work independently, therefore, the callback functions only rely one dropdown list selection at a time.

### Example 4 - Dropdown of Selections with Value different with Label displayed
This is an example on displaying readable label on the dropdown, and return programable text (value) in the backend. When select a choice from the dropdown list, it will display the text association with such selection for backend to consume. In this example, it will simply display that value.

### Example 5 - Cleaner Design and Select only from the Dropdown List
This example allows developer omit the textbox above the dropdown list for instruction, and place it in the dropdown list instead. The example also disable to clear the selection in the dropdown

### Example 6 - Disable Search in the Dropdown List
Users are expected to pick the selection without any typing.

## Reference
Plotly Documentation on Dropdown List <a href="https://dash.plotly.com/dash-core-components/dropdown" target="_blank">link</a>