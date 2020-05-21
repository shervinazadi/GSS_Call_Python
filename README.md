# GSS-Lab

This project is part of the stup fot Generative Sciences & Systems Lab Setup. It is currently being developed by [Shervin Azadi](https://github.com/shervinazadi) and [Pirouz Nouria](https://github.com/Pirouz-Nourian) at GSS-Lab, Department of Architectural Engineering and Technology, at TU Delft.

# Houdini Call Python Asset

This houdini asset allows the user to choose a python file and choose a specfic python environment and run the python script with the selected environment. This allows for separation of environments through a workflow and also solves the problem of importing libraries in houdini completely. This asset is compatible with conda environments as well.

This module uses the `sqlite3` standard library to replicate the houdini's geo database and passes the address to the subprocess. The sub process will read the database, execute the computational process and saves the data into the database. You can decide to keep or delete the database for trouble shooting distances. The input data is saved to tables named `"POINTS", "VERTICES", "PRIMITIVE", "DETAIL"` and the output data needs to be saved to tables named `"POINTS_NEW", "VERTICES_NEW", "PRIMITIVE_NEW", "DETAIL_NEW"`.

You can find an example python script along with the asset.

## Known Issues

- currently you need to have at least one attribute on prim and detail level for the node to work
- attribute names should not include the charachter "\_"
- currently all attributes are passed (before) and updated (after) by defualt
- currently there is no access to intrinsic attributes
- currently list attributes are not supported
- currently erors of the subprocess are lost

## Upcoming Features

- Support of selective attribute transfer to resduce the overhead
- Support of list attributes
- Support of intrinsic attributes
- Support of writing python code inside houdini interface
- Saving the databse file in the temp folder of the computer instead of the working directory
- Ability to create new attributes
- Ability to create and delete points
- Ability to create and delete primitives
- Catching the errors of the subprocess
