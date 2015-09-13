export default {
    // event
    trackStartApp() {
        if (typeof mixpanel === 'undefined') return;
        mixpanel.track('zy-start-app');
    },

    trackSearchEvent(keyword) {
        if (typeof mixpanel === 'undefined') return;
        mixpanel.track("zy-search", {
            'keyword': keyword
        });
    },
    trackPostClickEvent(pid, title) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-post-read", {
            'post_id': pid,
            'title': title
        });
    },
    trackCategoryClickEvent(cid) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-category-select", {
            'category_id': cid
        });
    },
    trackVendorClickEvent(vid) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-vendor-select", {
            'vendor_id': vid
        });
    },
    trackReadSource(pid, title) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-post-read-source", {
            'pid': pid,
            'title': title
        });
    },
    trackReadLater(pid, title) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-read-later", {
            'pid': pid,
            'title': title
        });
    },
    trackFav(pid, title) {
        if (typeof mixpanel === 'undefined') return; 
        mixpanel.track("zy-fav", {
            'pid': pid,
            'title': title
        });
    }
}
