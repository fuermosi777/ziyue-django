export default {
    init(item) {
        this.item = item;
    },

    getPosts() {
        let postsObject = JSON.parse(localStorage.getItem(`favPosts`));
        if (!postsObject) {
            localStorage.setItem(`favPostsIndex`, JSON.stringify([]));
            localStorage.setItem(`favPosts`, JSON.stringify([]));
            return [];
        }
        return postsObject;
    },

    getPost(postId) {
        let indexObject = JSON.parse(localStorage.getItem(`favPostsIndex`));
        if (!indexObject) return null;
        let targetIndex = indexObject.indexOf(postId);
        if (targetIndex === -1) return null;
        let postsObject = JSON.parse(localStorage.getItem(`favPosts`));
        let targetPost = postsObject[targetIndex];
        return {index: targetIndex, post: targetPost};
    },


    addPost(post) {
        /*
        let getPost = this.getPost(post.id);
        if (getPost) return false;
        */
        // add to index
        let indexObject = JSON.parse(localStorage.getItem(`favPostsIndex`));
        indexObject.push(post.id);
        localStorage.setItem(`favPostsIndex`, JSON.stringify(indexObject));
        // add actual post
        let postObject = JSON.parse(localStorage.getItem(`favPosts`));
        postObject.push(post);
        localStorage.setItem(`favPosts`, JSON.stringify(postObject));
        return true;
    },

    deletePost(postId) {
        let targetPost = this.getPost(postId);
        if (!targetPost) return false;
        let indexObject = JSON.parse(localStorage.getItem(`favPostsIndex`));
        indexObject.splice(targetPost.index, 1);
        localStorage.setItem(`favPostsIndex`, JSON.stringify(indexObject));
        let postObject = JSON.parse(localStorage.getItem(`favPosts`));
        postObject.splice(targetPost.index, 1);
        localStorage.setItem(`favPosts`, JSON.stringify(postObject));
        return true;
    }
}