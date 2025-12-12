import { Config } from "@/services/Config";

/**
 * Generic class for posting and fetching to a url
 */
export class HTTPService {

    /**
     * Fetch post
     * @param {Data} url -- endpoint URL
     * @param {TResponse} data -- object will be stringified and passed in the body
     * @returns {Promise<Response>}
     */
    static async post<Data, TResponse>(url: string, data: Data): Promise<TResponse> {
        try {
            const response = await fetch(url, {
                method: 'post',
                headers: { 'Content-Type': 'application/json; charset=UTF-8' },
                body: JSON.stringify(data),
                credentials: Config.DEV ? 'include' : 'same-origin'
            });

            HTTPService.validateResponse(response);
            return await response.json() as TResponse;
        } catch (error) {
            console.error(error);
            throw new Error('Failed to fetch from ' + url);
        }
    };

    /**
     * Fetch get
     * @param {Data} url -- endpoint URL
     * @param {TResponse} data -- object will converted to url query params
     * @returns {Promise<Response>}
     */
    static async get<Data, TResponse>(url: string, data?: Data): Promise<TResponse> {
        try {
            if (data) {
                const params = new URLSearchParams(data);
                url = `${url}?${params.toString()}`;
            }

            const response = await fetch(url, {
                method: 'get',
                headers: { 'Content-Type': 'application/json' },
                credentials: Config.DEV ? 'include' : 'same-origin'
            });

            HTTPService.validateResponse(response);
            return await response.json() as TResponse;
        } catch (error) {
            console.error(error);
            throw new Error('Failed to fetch from ' + url);
        }
    };

    static validateResponse(response: Response) {
        if (response.status === STATUS.FORBIDDEN) {
            throw new Error('Forbidden');
        } else if (response.status === STATUS.UNAUTHORIZED) {
            throw new Error('Unauthorized')
        }
    }
}

const STATUS = {
    UNAUTHORIZED: 401,
    FORBIDDEN: 403
}