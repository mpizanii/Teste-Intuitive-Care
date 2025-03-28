<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <div class="inputs">
      <input 
        v-model="query"
        @input="fetchResults"
        placeholder="Digite um termo para buscar..." 
      />
    </div>
    <ul>
      <li v-for="result in results" :key="result.registro_ans">
        <span v-html="`Nome: ${result.nome_fantasia}<br>Razão Social: ${result.razao_social}<br>Cidade: ${result.cidade}<br>UF: ${result.UF}`"></span>
      </li>
    </ul>
  </div>
</template>

<script>
import { fetchResults } from '../services/apiService';

export default {
  data() {
    return {
      query: '',
      results: [],
    };
  },
  methods: {
    async fetchResults() {
      if (!this.query.trim()) {  
        this.results = [];
        return;
      }
      try {
        this.results = await fetchResults(this.query);
      } catch (error) {
        console.error('Erro ao buscar:', error);
        this.results = []; 
      }
    },
  },
};
</script>

<style src="../assets/css/style.css"></style>