################ Copyright 2005-2013 Team GoldenEye: Source #################
#
# This file is part of GoldenEye: Source's Python Library.
#
# GoldenEye: Source's Python Library is free software: you can redistribute 
# it and/or modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation, either version 3 of the License, 
# or(at your option) any later version.
#
# GoldenEye: Source's Python Library is distributed in the hope that it will 
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General 
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GoldenEye: Source's Python Library.
# If not, see <http://www.gnu.org/licenses/>.
#############################################################################
from GEAi import ActivityId
from . import BaseSchedule, Cond
from ..Tasks import Task

class EstablishLOFFallback( BaseSchedule ):
    def Build( self ):
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.GET_CHASE_PATH_TO_ENEMY )
        self.AddTask( Task.RUN_PATH_TIMED, 2 )
        self.AddTask( Task.WAIT_FOR_MOVEMENT )

        self.AddInterrupt( Cond.CAN_RANGE_ATTACK1 )
        self.AddInterrupt( Cond.CAN_MELEE_ATTACK1 )

class CombatFaceOverride( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.ESTABLISH_LINE_OF_FIRE )
        self.AddTask( Task.STOP_MOVING )
        self.AddTask( Task.SET_ACTIVITY, ActivityId( "ACT_IDLE" ) )
        self.AddTask( Task.FACE_ENEMY )

        self.AddInterrupt( Cond.CAN_RANGE_ATTACK1 )
        self.AddInterrupt( Cond.CAN_MELEE_ATTACK1 )
        self.AddInterrupt( Cond.NEW_ENEMY )
        self.AddInterrupt( Cond.ENEMY_DEAD )

class BotSeekEnemy( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.BOT_PATROL )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 48 )
        self.AddTask( Task.GES_FIND_ENEMY )
        self.AddTask( Task.GET_PATH_TO_TARGET )
        self.AddTask( Task.RUN_PATH_TIMED, 5.0 )

        self.AddInterrupt( Cond.NEW_ENEMY )
        self.AddInterrupt( Cond.LIGHT_DAMAGE )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.HEAR_COMBAT )
        self.AddInterrupt( Cond.GES_CLOSE_TO_ARMOR )

class BotEngageEnemy( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.ESTABLISH_LINE_OF_FIRE )
        self.AddTask( Task.STORE_POSITION_IN_SAVEPOSITION )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 25 )
        self.AddTask( Task.GET_FLANK_RADIUS_PATH_TO_ENEMY_LOS, 250 )
        self.AddTask( Task.RUN_PATH_TIMED, 1.5 )
        self.AddTask( Task.WAIT_FOR_MOVEMENT )

        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.ENEMY_DEAD )
        self.AddInterrupt( Cond.GES_ENEMY_CLOSE )
        self.AddInterrupt( Cond.ENEMY_UNREACHABLE )
        self.AddInterrupt( Cond.ENEMY_WENT_NULL )

class BotPatrol( BaseSchedule ):
    def Build( self ):
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.GET_PATH_TO_RANDOM_NODE, 2048 )
        self.AddTask( Task.RUN_PATH_WITHIN_DIST, 20 )
        self.AddTask( Task.CLEAR_GOAL )
        self.AddTask( Task.GET_PATH_TO_RANDOM_NODE, 2048 )
        self.AddTask( Task.RUN_PATH_WITHIN_DIST, 20 )
        self.AddTask( Task.WAIT_RANDOM, 1.0 )

        self.AddInterrupt( Cond.NO_PRIMARY_AMMO )
        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.HEAR_COMBAT )
        self.AddInterrupt( Cond.HEAR_BULLET_IMPACT )
        self.AddInterrupt( Cond.NEW_ENEMY )
        self.AddInterrupt( Cond.SEE_ENEMY )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.LIGHT_DAMAGE )
        self.AddInterrupt( Cond.GES_CLOSE_TO_ARMOR )
        self.AddInterrupt( Cond.GES_CLOSE_TO_WEAPON )

class BotSeekWeapon( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.BOT_PATROL )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 48 )
        self.AddTask( Task.GES_FIND_WEAPON, 1024 )
        self.AddTask( Task.GET_PATH_TO_TARGET )
        self.AddTask( Task.WEAPON_RUN_PATH, 8 )

        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.GES_ENEMY_CLOSE )
        self.AddInterrupt( Cond.GES_ENEMY_DANGEROUS )

class BotSeekAmmo( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.BOT_PATROL )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 48 )
        self.AddTask( Task.GES_FIND_AMMO, 1024 )
        self.AddTask( Task.GET_PATH_TO_TARGET )
        self.AddTask( Task.ITEM_RUN_PATH, 8 )

        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.LIGHT_DAMAGE )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.GES_ENEMY_DANGEROUS )

class BotSeekArmor( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.BOT_PATROL )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 48 )
        self.AddTask( Task.GES_FIND_ARMOR, 2048 )
        self.AddTask( Task.GET_PATH_TO_TARGET )
        self.AddTask( Task.ITEM_RUN_PATH, 8 )

        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )
        self.AddInterrupt( Cond.GES_ENEMY_DANGEROUS )
        self.AddInterrupt( Cond.GES_ENEMY_CLOSE )

class BotSeekToken( BaseSchedule ):
    def Build( self ):
        from . import Sched

        self.AddTask( Task.SET_FAIL_SCHEDULE, Sched.BOT_PATROL )
        self.AddTask( Task.SET_ROUTE_SEARCH_TIME, 2 )
        self.AddTask( Task.SET_TOLERANCE_DISTANCE, 48 )
        self.AddTask( Task.GES_FIND_TOKEN )
        self.AddTask( Task.GET_PATH_TO_TARGET )
        self.AddTask( Task.ITEM_RUN_PATH, 8 )

        self.AddInterrupt( Cond.HEAR_DANGER )
        self.AddInterrupt( Cond.GES_ENEMY_CLOSE )
        self.AddInterrupt( Cond.LIGHT_DAMAGE )
        self.AddInterrupt( Cond.HEAVY_DAMAGE )

