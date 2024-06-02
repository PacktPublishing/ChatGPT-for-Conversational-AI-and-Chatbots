const { OpenAIAPI } = require('openai'); 

const openai = new OpenAIAPI({ key: "your-openai-api-key-here" }); // Replace with your actual OpenAI API key 

async function chatWithGPT(model, userMessage, topP = 1, frequencyPenalty = 0, presencePenalty = 0, temperature = 0) { 

  try { 

    	const prompt = userMessage; 
	const maxTokens = 100; 
	const chatResponse = await openai.chat.completions.create({ 
	model: model,messages: [{ 
		role: "user", 
		content: prompt 
		}], 
	temperature: temperature, 
	top_p: topP, 
	frequency_penalty: frequencyPenalty, 
	presence_penalty: presencePenalty, 
	max_tokens: maxTokens 
	}); 
	return chatResponse.data; 
} catch (error) { 
	return error.toString(); 
}} 


async function main() { 

    try { 
    
        const response = await chatWithGPT("gpt-3.5-turbo", "Hello world", 0.9, -0.5, 0.6);     
    
    console.log("ChatGPT Response:", response.data); 
    } catch (error) { 
        console.error("Error:", error); 
    
    }} 


    main()