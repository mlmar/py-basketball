import { Config } from "@/services/Config";
import { HTTPService } from "@/services/HTTPService";

const AUTH_SERVICE_URL = Config.SERVER_URL

export class AuthService {
    /**
     * Retrieves user details
     * @returns current user
     */
    static async validateUser(): Promise<boolean> {
        const response = await HTTPService.get<null, boolean>(AUTH_SERVICE_URL + '/validate');
        return response;
    }
}