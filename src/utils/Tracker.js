export default {
    
    // page view
    trackCategoryPageView(category) {
        if (typeof GA === 'undefined') return;
        GA('send', 'pageview', '/' + category);
    },
    trackPostPageView(pid) {
        if (typeof GA === 'undefined') return;
        GA('send', 'pageview', '/post/' + pid);
    },
    trackVendorPageView(vid) {
        if (typeof GA === 'undefined') return;
        GA('send', 'pageview', '/vendor/' + vid);
    }
}