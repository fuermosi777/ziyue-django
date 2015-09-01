let urlPrefix = ZYIsDev ? 'http://localhost:8000' : '';

export default {
    posts(category, start=0) {
        return `${urlPrefix}/api/posts/?category=${category}&start=${start}`;
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