export default {
    init(item) {
        this.item = item;
    },

    getPosts() {
        let postsObject = JSON.parse(localStorage.getItem(`readLaterPosts`));
        if (!postsObject) {
            localStorage.setItem(`readLaterPostsIndex`, JSON.stringify([]));
            localStorage.setItem(`readLaterPosts`, JSON.stringify([]));
            return [];
        }
        return postsObject;
    },

    getPost(postId) {
        let indexObject = JSON.parse(localStorage.getItem(`readLaterPostsIndex`));
        if (!indexObject) return null;
        let targetIndex = indexObject.indexOf(postId);
        if (targetIndex === -1) return null;
        let postsObject = JSON.parse(localStorage.getItem(`readLaterPosts`));
        let targetPost = postsObject[targetIndex];
        return {index: targetIndex, post: targetPost};
    },


    addPost(post) {
        /*
        let getPost = this.getPost(post.id);
        if (getPost) return false;
        */
        // add to index
        let indexObject = JSON.parse(localStorage.getItem(`readLaterPostsIndex`));
        indexObject.push(post.id);
        localStorage.setItem(`readLaterPostsIndex`, JSON.stringify(indexObject));
        // add actual post
        let postObject = JSON.parse(localStorage.getItem(`readLaterPosts`));
        postObject.push(post);
        localStorage.setItem(`readLaterPosts`, JSON.stringify(postObject));
        return true;
    },

    deletePost(postId) {
        let targetPost = this.getPost(postId);
        if (!targetPost) return false;
        let indexObject = JSON.parse(localStorage.getItem(`readLaterPostsIndex`));
        indexObject.splice(targetPost.index, 1);
        localStorage.setItem(`readLaterPostsIndex`, JSON.stringify(indexObject));
        let postObject = JSON.parse(localStorage.getItem(`readLaterPosts`));
        postObject.splice(targetPost.index, 1);
        localStorage.setItem(`readLaterPosts`, JSON.stringify(postObject));
        return true;
    }
}