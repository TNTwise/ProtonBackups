# This Program allows you to create snapshots of Proton Experimental and bleeding edge builds.
This will create a snapshot of the current Proton Experimental build downloaded to the computer. <br />
If you are creating an Experimental snapshot, it will look like Ex-(Date it was created) <br />
If you are creating an Experimental bleeding edge snapshot, it will look like ExBE-(Version) <br />
To run the program,
1. Clone the repo.
```bash
git clone https://github.com/TNTwise/ProtonExperimentalBuilds.git
```
2. Entering the directory.
```bash
cd ProtonExperimentalBuilds
```
3. Running the script.
```bash
python get_latest_proton_experimental.py
```
4. The extracted proton version will be in your /home/$USER/Downloads/ directory.

# Note, I did not create proton, I am just uploading snapshots of https://github.com/ValveSoftware/Proton Experimental and bleeding-edge builds.

To run a build, 
1. Download a build from the releases tab. 
2. Extract it to /home/$USER/.steam/steam/compatibilitytools.d/.
3. In steam, go to the games settings, -> properties -> compatibility.
4. Check Force the use of a specific Steam Play compatibility tool.
5. click on the ExBE or Ex version of proton.

Should probably add automatically detect if it is an experimental build or bleeding edge and delete the right version.
Maybe add an automatically download and install intro compadibility tools folder script.
