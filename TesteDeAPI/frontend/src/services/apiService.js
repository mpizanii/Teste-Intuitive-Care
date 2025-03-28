import axios from 'axios';

export const fetchResults = async (query) => {
  if (query.trim().length > 2) { 
    try {
      const response = await axios.get('http://127.0.0.1:8000/buscar/', {
        params: { q: query },
      });
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar os resultados:', error);
      
      throw new Error('Erro ao buscar resultados. Verifique o servidor ou o formato do termo.');
    }
  }

  return [];  
};