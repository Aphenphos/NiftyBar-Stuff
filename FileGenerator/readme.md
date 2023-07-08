Basic File creator for consistent directory and file generation  
  
Probably should use a .env file in the future for constants  
  
GUI primarily used to ease the tedium of keeping a neat and orderly file structure.  
  
    
Customer Name is considered a Home directory of sorts that will house all of the jobs related to that customer.  
DXF and DIG files are automatically generated with the JOB name for ease of future reference and documentation. Upon submitting a Customer and Job the directory will be found (if it doesnt exist it will be created) and a Job specific subdirectory will also be created for that customer. This folder will then have automatically generated and named DXF (TurboCAD) file and a generated and named DIG (IGems) file for ease of access. The program will also automatically open both of these files in their respective programs.  
WILL ADD OPTIONAL ABILITY TO TURN OFF AUTO OPENING OF IGEMS AND TURBOCAD TO ALLOW QUICK CREATION OF MANY JOB DIRECTORIES BACK TO BACK.
