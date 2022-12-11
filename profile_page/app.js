import axios from 'axios';

const formResponses = document.getElementsByName('formEditProfile');

const fn = document.querySelector('.fn');
const ln = document.querySelector('.ln');
const age = document.querySelector('.age');
const desc = document.querySelector('.desc');

var query = window.location.search.substring(1);
var code = query.split("=");
var value = code[1];
var values = value.split("-");
var age_int = values[2];
const fn_val = values[0];
const ln_val = values[1];
const age_val = parseInt(age_int);
const desc_val = values[3];

fn.textContent = `First Name   : ${fn_val}`;
ln.textContent = `Last Name    : ${ln_val}`;
age.textContent = `Age          : ${age_val}`;
desc.textContent = `Description  : ${desc_val}`;

const API_URL = `https://strapi-production-ef0a.up.railway.app`;
         const token = `Bearer f9f56b73b73070e6006352dc14cce6ee5e74840295ecc1dff3fd288029acf9844d60e6849c1f34cc7d510a2007367962dd5d6574c46e33307572782c9a592552609ec4b892294b19196e460e09b3760046365a4fcf4d2966d886cf0351cafc630d8323ad1fc5ec3539c7de011bc855ea6fd51783b3b59f9e2a29b4485b5d6f52`;
         let path = `api/calendar-users`;
         
         axios
            .post(URL,{
               headers: {
                  Authorization: token,
               },
            })
            .then(response => {
               console.log(response.data);
            })
            .catch(error => {
               console.log(error.response);
            })
         
         
         // const getdata = ({}) => {
         //    const fetch = async (token) =>{
         //       try {
         //          const URL = API_URL + "/" + path;
         //          const res = await fetch(URL, {
         //             headers: { Authorization: `${token}` },
         //          });
         //          const data = await response.json();
         //       } catch (error){
         //          console.error(error);
         //       } 
         //    }
         // }
         
         // export default fetch;