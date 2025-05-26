// http_tight.js (120 lines)
const axios = require('axios');

class ProductService {
    async getProduct(id) {
        const response = await axios.get(`https://api.store.com/products/${id}`);
        return response.data;
        // Tight Coupling: Hardcoded Axios. Hard to mock in tests.
    }
}
