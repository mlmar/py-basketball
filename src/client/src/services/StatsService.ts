import { Config } from "@/services/Config";
import { HTTPService } from "@/services/HTTPService";

const STATS_SERVICE_URL = Config.SERVER_URL;

export class StatsService {

    /**
     * Retrieves player averages from the last N days
     * @param {number} days 
     * @returns 
     */
    static async getAverages(days: number = 0) {
        days = days || 0;
        const response = await HTTPService.get<{ days: number }, unknown[]>(STATS_SERVICE_URL + '/averages/' + days);
        return response;
    }
}