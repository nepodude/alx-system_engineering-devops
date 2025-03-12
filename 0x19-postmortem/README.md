Our service for sending money wasn't functional on 11th February 2025 from 13:21 EAT to 19:40 EAT due to a buggy file that was pushed on the platform on 11th February 2025 at 13:20 EAT. We detected it due to complaints of clients who attempted to send money and it showed a blank page instead.
Time:
. Time of detection:  11th Feb 2025 13:25 EAT
. How we detected it: Through clients complaints.
. Actions taken: Fixing platform backend.
. Misleading paths: We thought the problem was frontend but later we realized it was indeed on the backend.
. How we resolved the incident: We investigated all files contributing to the Backend side of the financial transaction of our platform and we found that the file that was pushed at 13:20 had a line of code that comfused the platform becuase it created multiple operations which made the server busy and not able to render the required information.

We apologize to any inconveniances this might cause to our platform users. We have taken measures to ensure the realiablity of our platform in the future. We have taken the following measures:

. We have established a team of software engineers responsible to review the code before allowing it to take effect on our platform.
. We have integrated AI that is responsible of running all our platforms tests for the pushed code to check for it's validity.