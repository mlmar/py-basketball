import { Config } from "@/services/Config";
import { HTTPService } from "@/services/HTTPService";
import type { AnalysisResult } from "@/services/types/AnalysisResult";
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
    static async getProjectedAnalysis(limit: number = -1): Promise<AnalysisResult<ProjectedPlayer>> {
        const response = await HTTPService.get<{ limit: number }, AnalysisResult<ProjectedPlayer>>(STATS_SERVICE_URL + '/projected-analysis', { limit });
        return response;
    }

    /**
     * Retrieves most recent trending analysis
     * @returns 
     */
    static async getTrendingAnalysis(limit: number = -1): Promise<AnalysisResult<TrendingPlayer>> {
        const response = await HTTPService.get<{ limit: number }, AnalysisResult<TrendingPlayer>>(STATS_SERVICE_URL + '/trending-analysis', { limit });
        return response;
    }
}