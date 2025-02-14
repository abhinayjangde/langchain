import Groq from "groq-sdk";
import {loadEnvFile} from "process"

loadEnvFile()

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

const getModels = async () => {
  return await groq.models.list();
};

getModels().then((models) => {
  console.log(models);
}).catch(err=>console.log(err))
