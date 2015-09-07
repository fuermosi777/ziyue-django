import $ from 'jquery';

export default {
    GET(url) {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: url,
                dataType: 'json',
                success(res) {
                    resolve(res);
                },
                error(err) {
                    console.log(err);
                    reject(err);
                }
            });
        });
    },
    POST(url, data) {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: url,
                type: 'POST',
                dataType: 'json',
                data: data,
                success(res) {
                    resolve(res);
                },
                error(err) {
                    console.log(err);
                    reject(err);
                }
            })
        });
    },

    findPostBasedOnId(posts, postId) {
        let findIndex;
        let find = posts.filter((item, i) => {
            if (item.id === postId) {
                findIndex = i;
                return item;
            }
        });
        if (find.length > 0) {
            return findIndex;
        } else {
            return -1;
        }
    }
}