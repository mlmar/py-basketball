import { Config } from "@/services/Config";
import { HTTPService } from "@/services/HTTPService";

const YAHOO_SERVICE_URL = Config.SERVER_URL + '/yahoo'

export class YahooService {
    /**
     * Retrieves user details
     * @returns current user
     */
    static async validateUser(): Promise<boolean> {
        try {
            const response = await HTTPService.get<null, boolean>(YAHOO_SERVICE_URL + '/validate');
            return response;
        } catch {
            return false;
        }
    }
}