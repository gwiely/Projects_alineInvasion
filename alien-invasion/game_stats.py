class GameStats():
    """跟踪游戏统计信息的类"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏启动时处于活动状态
        self.game_active = False
        # 计分
        self.score = 0
        # 任何情况下都不应重置最高分和当前得分的图像
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
