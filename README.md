# ue_batch_renamer

A simple and efficient batch renaming tool for Unreal Engine assets. This tool allows you to quickly and easily rename multiple assets in your project based on asset types, with customizable prefixes.

Tested on UE 5.3 & 5.4

                                      
                                      
                                                              Before 

![image](https://github.com/user-attachments/assets/bc086f42-e850-453e-b69c-1042b1bb4456)

                     
                                                              After
                            
![image](https://github.com/user-attachments/assets/32b8b299-3657-46f9-b1db-1f428a99c636)
                            

                          

**Features**

1. Automatically adds the correct prefix based on asset type (e.g., SM_ for Static Meshes, MAT_ for Materials).

2. Supports custom prefixes for assets (e.g., to add your own unique identifier).

3. Removes any existing known prefixes before renaming.

4. Works with selected assets directly from the Content Browser.

**Supported Asset Types**


1. Static Meshes

2. Materials

3. Material Instances

4. Textures

5. Blueprints

6. Niagara Systems

7. Skeletal Meshes

8. Levels

9. Level Sequences


**Requirements**

Unreal Engine 5.3 or 5.4

Python Editor Script Plugin Enabled

**Installation**

1. Download the Python script.

2. Open the Unreal Editor.

3. Run the script using the Python Editor inside Unreal. (Tools > execute python script..)
   

**How to Use**

1. Select the assets you want to rename in the Content Browser.

2. Run the script to automatically rename the selected assets based on their type.

3. Optionally, specify a custom prefix to be applied to all assets.



**_Feel free to get your suggestions or improvements!_**
