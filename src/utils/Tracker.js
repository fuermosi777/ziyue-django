export default {
    
    // page view
    trackCategoryPageView(category) {
        GA('send', 'pageview', '/' + category);
    },
    trackPostPageView(pid) {
        GA('send', 'pageview', '/post/' + pid);
    },
    trackVendorPageView(vid) {
        GA('send', 'pageview', '/vendor/' + vid);
    },

    // event
    trackSearchEvent(keyword) {
        GA('send', 'event', 'search', 'zy-search', keyword);
    },
    trackPostClickEvent(eid) {
        GA('send', 'event', 'post', 'zy-post-read', eid);
    },
    trackCategoryClickEvent(cid) {
        GA('send', 'event', 'category', 'zy-category-select', cid);
    },
    trackReadSource(pid) {
        GA('send', 'event', 'post', 'zy-post-read-source', pid);
    },
    trackReadLater() {
        GA('send', 'event', 'site', 'zy-read-later');
    },
    trackFav() {
        GA('send', 'event', 'site', 'zy-fav');
    }
}