# Houdini Call Python Asset

This houdini asset allows the user to choose a python file and choose a specfic python environment and run the python script with the selected environment. This allows for separation of environments through a workflow and also solves the problem of importing libraries in houdini completely. This asset is compatible with conda environments as well.

This module uses the `sqlite3` standard library to replicate the houdini's geo database and passes the address to the subprocess. The sub process will read the database, execute the computational process and saves the data into the database. You can decide to keep or delete the database for trouble shooting purposes.

## Usage

- attribute names should not include the charachter "\."
- You can select the attributes that you want to pass to database through the houdini interface. If you leave the selection field empty it will pass all the attributes by defualt. Passing all the attributes adds extra overhead.
- The input data is saved to database under tables: `"POINTS", "VERTICES", "PRIMITIVE", "DETAIL"`.
- the output data needs to be saved to database under tables: `"POINTS_NEW", "VERTICES_NEW", "PRIMITIVE_NEW", "DETAIL_NEW"`
- users should selectively pass data to the subprocess and back since it affects the overhead directly
- You can find an example python script along with the asset. In the example file I am using `pandas` to load the data from database and dump the data into it afterwards. You can use your own library of choice.

## Features

- Run python code in any environment in connection to houdini geometry database
- selectively pass the attributes for efficiency
- create new attributes within the subprocess
- create and delete points within the subprocess
- initiate and delete primitives within the subprocess
- output the database for trouble shooting purposes
- Support of writing python code inside houdini interface

## Known Issues

- currently list attributes are not supported
- currently errors of the subprocess are not caught
- vertices can not be created or added to primitives

## Upcoming Features

- Support of list attributes
- Suppot of adding and removing vertices to and from primitives within the subpocess
- Catching the errors of the subprocess
- py file watcher

---

# GSS-Lab

This project is part of the stup fot Generative Sciences & Systems Lab Setup. It is currently being developed by [Shervin Azadi](https://github.com/shervinazadi) and [Pirouz Nourian](https://github.com/Pirouz-Nourian) at GSS-Lab, Department of Architectural Engineering and Technology, at TU Delft.
