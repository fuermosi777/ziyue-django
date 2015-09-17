import {POST} from '../utils/Basic';

export default {
    getFont(body) {
        return POST('/font/main/', {
            body: body
        });
    }
}