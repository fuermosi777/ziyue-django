let urlPrefix = ZYIsDev ? 'http://localhost:8000' : 'http://ziyue.io';

export default {
    posts(category, start=0) {
        return `${urlPrefix}/api/posts/?category=${category}&start=${start}`;
    },
    recommendPosts(post_id) {
        return `${urlPrefix}/api/posts/recommend/?post_id=${post_id}`;
    },
    vendors(category) {
        return `${urlPrefix}/api/vendors/?category=${category}`;
    },
    vendorPosts(vendorId, start=0) {
        return `${urlPrefix}/api/vendor/posts/?vendor_id=${vendorId}&start=${start}`;
    },
    post(post_id) {
    	return `${urlPrefix}/api/post/?post_id=${post_id}`;
    },
    searchPosts(q, start) {
        return `${urlPrefix}/api/post/search/?q=${q}&start=${start}`
    },
    searchVendors(keyword) {
        return `${urlPrefix}/api/search/vendors/?q=${keyword}`;
    }
};