import Basic from '../utils/Basic.js';
import Urls from '../utils/Urls.js';
import Constant from '../utils/Constant.js';

export default {
    getCategorys() {
        return Promise.resolve(Constant.CATEGORYS);
    },

    getPosts(category, start=0) {
        return Basic.GET(Urls.posts(category, start));
    },

    getPost(id) {
    	return Basic.GET(Urls.post(id));
    },

    searchPosts(q, start=0) {
        return Basic.GET(Urls.searchPosts(q, start));
    },

    getVendors(keyword) {
        return Basic.GET(Urls.vendors(keyword));
    },

    getVendorPosts(vendorId, start=0) {
        return Basic.GET(Urls.vendorPosts(vendorId, start));
    }
};