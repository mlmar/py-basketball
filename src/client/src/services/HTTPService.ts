/**
 * Generic class for posting and fetching to a url
 */
export class HTTPService {

    /**
     * Fetch post
     * @param {T} url -- endpoint URL
     * @param {Response} data -- object will be stringified and passed in the body
     * @returns {Promise<Response>}
     */
    static async post<T, Response>(url: string, data: T): Promise<Response> {
        try {
            const response = await fetch(url, {
                method: 'post',
                headers: { 'Content-Type': 'application/json; charset=UTF-8' },
                body: JSON.stringify(data),
            });

            return await response.json();
        } catch (error) {
            console.error(error);
            throw new Error('Failed to fetch from ' + url);
        }
    };

    /**
     * Fetch get
     * @param {T} url -- endpoint URL
     * @param {Response} data -- object will converted to url query params
     * @returns {Promise<Response>}
     */
    static async get<T, Response>(url: string, data?: T): Promise<Response> {
        try {
            if (data) {
                const params = new URLSearchParams(data);
                url = `${url}?${params.toString()}`;
            }

            const response = await fetch(url, {
                method: 'get',
                headers: { 'Content-Type': 'application/json' },
            });

            return await response.json() as Response;
        } catch (error) {
            console.error(error);
            throw new Error('Failed to fetch from ' + url);
        }
    };
}