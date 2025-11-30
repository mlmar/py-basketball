import { Config } from "@/services/Config";
import { HTTPService } from "@/services/HTTPService";
import type { ProjectedPlayer } from "@/services/types/ProjectedPlayer";
import type { TrendingPlayer } from "@/services/types/TrendingPlayer";

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

    /**
     * Retrieves most recent analysis
     * @returns 
     */
    static async getProjectedAnalysis(): Promise<ProjectedPlayer[]> {
        const response = await HTTPService.get<{ days: number }, ProjectedPlayer[]>(STATS_SERVICE_URL + '/projected-analysis');
        return response;
    }

    /**
     * Retrieves most recent trending analysis
     * @returns 
     */
    static async getTrendingAnalysis(): Promise<TrendingPlayer[]> {
        const response = await HTTPService.get<{ days: number }, TrendingPlayer[]>(STATS_SERVICE_URL + '/trending-analysis');
        return response;
    }
}