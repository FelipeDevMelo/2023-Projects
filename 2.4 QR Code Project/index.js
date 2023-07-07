/* 
1. Use the inquirer npm package to get user input.
2. Use the qr-image npm package to turn the user entered URL into a QR code image.
3. Create a txt file to save the user input using the native fs node module.
*/
import inquirer from 'inquirer';
import qr from 'qr-image';


const prompts = [
    {
      type: 'input',
      name: 'URL',
      message: 'Type the Url to turn into a QR code: ',
    },
  ];
  
  inquirer.prompt(prompts).then(answers => {
    console.log('Hello, ' + answers.URL+ '!');
  });
  